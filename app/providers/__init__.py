from abc import ABC, abstractmethod


class ImageGeneratorProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs):
        pass


from app.providers.dalle import DalleGeneratorProvider  # noqa
from app.providers.openai import OpenAIGeneratorProvider  # noqa
from app.providers.stable_diffusion import StableDiffusionProvider  # noqa
from app.providers.context import ImageGeneratorContext  # noqa
