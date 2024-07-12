import asyncio
import os
import sys

import pika
from pika.adapters.blocking_connection import BlockingChannel

from app.services import RabbitMQContext
from app.utils import setup_logger

logger = setup_logger(__name__)


def message_processor(
    channel: BlockingChannel,
    method: pika.spec.Basic.Deliver,
    properties: pika.spec.BasicProperties,
    body: bytes,
) -> None:
    logger.info(f"Processing message: {body.decode()}")


async def openai_listener():
    with RabbitMQContext(queue="openai") as client:
        while True:
            client.consume(message_processor)


async def sd_listener():
    with RabbitMQContext(queue="stable_diffusion") as client:
        while True:
            client.consume(message_processor)


async def main():
    await asyncio.gather(sd_listener(), openai_listener())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.critical("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
