from typing import Callable

import pika
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from pika.connection import ConnectionParameters
from pika.credentials import PlainCredentials

from app.utils import rabbit_mq_config, setup_logger

logger = setup_logger(__name__)


class RabbitMQListener:
    def __init__(
        self,
        queue,
    ) -> None:
        """
        Initialize the RabbitMQListener by establishing a connection to the RabbitMQ server
        and setting up the channel.
        """
        logger.info("Peering to RabbitMQ Server")

        self.queue = queue

        credentials = PlainCredentials(
            username=rabbit_mq_config.USERNAME,
            password=rabbit_mq_config.PASSWORD,
            erase_on_connect=True,
        )

        conn_params = ConnectionParameters(
            host=rabbit_mq_config.HOST,
            port=rabbit_mq_config.PORT,
            credentials=credentials,
        )

        self.connection: BlockingConnection = BlockingConnection(conn_params)

        self.channel: BlockingChannel = self.connection.channel()

    def consume(self, callback: Callable):
        """
        Start consuming messages from the specified queue using the provided callback function.

        :param queue: The name of the queue to consume messages from.
        :param callback: The callback function to process the messages.
        """
        try:
            self.channel.queue_declare(queue=self.queue, durable=True)

            def on_message(
                channel: BlockingChannel,
                method: pika.spec.Basic.Deliver,
                properties: pika.spec.BasicProperties,
                body: bytes,
            ) -> None:
                """
                Internal method to handle incoming messages and delegate to the provided callback.

                :param channel: The channel object.
                :param method: Delivery method.
                :param properties: Properties of the message.
                :param body: The message body.
                """
                try:
                    logger.info(f"Received message: {body}")
                    callback(channel, method, properties, body)
                    channel.basic_ack(delivery_tag=method.delivery_tag)
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

            self.channel.basic_consume(
                queue=self.queue,
                on_message_callback=on_message,
                auto_ack=False,
            )

            logger.info(f"Started consuming messages from queue: {self.queue}")

            self.channel.start_consuming()
        except Exception as e:
            logger.exception("Error RabbitMQ consuming messages: ", e)

    def close(self) -> None:
        """
        Close the channel and the connection to RabbitMQ.
        """
        try:
            if self.channel.is_open:
                self.channel.close()
                logger.info("RabbitMQ Channel closed.")
            if self.connection.is_open:
                self.connection.close()
                logger.info("RabbitMQ connection closed.")
        except Exception as e:
            logger.error(f"Error closing the RabbitMQ connection: {e}")


class RabbitMQContext:
    def __init__(
        self,
        queue: str = rabbit_mq_config.QUEUE,
    ) -> None:
        self.service = RabbitMQListener(queue)

    def __enter__(self):
        return self.service

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            logger.exception("RabbitMQ error occurred: ", exc_value)
        self.service.close()
