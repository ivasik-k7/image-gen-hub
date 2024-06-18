from app.providers import ImageGeneratorProvider
from app.utils import setup_logger

logger = setup_logger(__name__)


class DalleGeneratorProvider(ImageGeneratorProvider):
    def generate(self, prompt: str, **kwargs):
        print("Dalle provider!")
