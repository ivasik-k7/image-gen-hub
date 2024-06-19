import os


class AppConfig:
    @property
    def STABLE_DIFFUSION_MODEL(self):
        return os.environ.get(
            "STABLE_DIFFUSION_MODEL", "stabilityai/stable-diffusion-2-1"
        )

    @property
    def MOBIUS_MODEL(self):
        return os.environ.get("MOBIUS_MODEL", "Corcelio/mobius")


class RabbitMQConfig:
    @property
    def QUEUE(self):
        return os.environ.get("RABBIT_MQ_QUEUE", "GENERATIONS")

    @property
    def HOST(self):
        return os.environ.get("RABBITMQ_HOST", "localhost")

    @property
    def PORT(self):
        return os.environ.get("RABBITMQ_PORT", "5672")

    @property
    def USERNAME(self):
        return os.environ.get("RABBITMQ_USERNAME", "admin")

    @property
    def PASSWORD(self):
        return os.environ.get("RABBIT_MQ_PASSWORD", "secret")


config = AppConfig()
rabbit_mq_config = RabbitMQConfig()
