if __name__ == "__main__":
    from app.services.rabbitmq import RabbitMQPublisher
    from app.utils import rabbit_mq_config

    publisher = RabbitMQPublisher(rabbit_mq_config.QUEUE)

    publisher.send("hello world!")
