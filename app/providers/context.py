from app.providers import ImageGeneratorProvider, StableDiffusionProvider
from app.utils import setup_logger

logger = setup_logger(__name__)


class ImageGeneratorContext:
    def __init__(
        self,
        provider: ImageGeneratorProvider = StableDiffusionProvider(),
    ) -> None:
        logger.info(f"ImageGeneratorContext initialized with {type(provider)} type.")
        self._provider = provider

    def __enter__(self):
        return self._provider

    def __exit__(self, exc_type, exc_value, stacktrace):
        if exc_type:
            logger.exception(
                f"While executing of ImageGeneratorContext error occurred: {exc_value}\nStacktrace: {stacktrace}"
            )
