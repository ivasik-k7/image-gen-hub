from app.providers import ImageGeneratorProvider
from app.utils import setup_logger

logger = setup_logger(__name__)


class OpenAIGeneratorProvider(ImageGeneratorProvider):
    def generate(self, prompt: str, **kwargs):
        logger.info(f"OpenAi Generator provider with prompt of {prompt}")
