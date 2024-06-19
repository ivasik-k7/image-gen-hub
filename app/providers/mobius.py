import torch
from diffusers import (
    AutoencoderKL,
    KDPM2AncestralDiscreteScheduler,
    StableDiffusionXLPipeline,
)

from app.providers import ImageGeneratorProvider
from app.utils import config


class MobiusGeneratorProvider(ImageGeneratorProvider):
    def __init__(self) -> None:
        self.model_id = config.MOBIUS_MODEL
        self.is_cuda_available = torch.cuda.is_available()
        self.pipe = None
        self.vae = None

    @property
    def device(self):
        return "cuda" if self.is_cuda_available else "cpu"

    def generate(self, prompt: str, **kwargs):
        self._load_vae()
        self._load_pipeline()

    def _load_pipeline(self):
        if not self.vae:
            raise RuntimeError("Vae has not been initialized!")

        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            self.model_id,
            vae=self.vae,
            torch_dtype=torch.float16,
        )
        self.pipe.scheduler = KDPM2AncestralDiscreteScheduler.from_config(
            self.scheduler.config
        )

        self.pipe.to(self.device)

    def _load_vae(self):
        self.vae = AutoencoderKL.from_pretrained(
            "madebyollin/sdxl-vae-fp16-fix",
            torch_dtype=torch.float16,
        )
