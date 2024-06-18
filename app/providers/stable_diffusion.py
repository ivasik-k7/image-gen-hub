from diffusers import (
    DiffusionPipeline,
    DPMSolverMultistepScheduler,
    StableDiffusionPipeline,
)

from app.providers import ImageGeneratorProvider
from app.utils import config, setup_logger

logger = setup_logger(__name__)


class StableDiffusionProvider(ImageGeneratorProvider):
    def __init__(
        self,
        model_id: str = config.STABLE_DIFFUSION_MODEL,
        use_safetensors: bool = True,
    ) -> None:
        self.model_id = model_id
        self.use_safetensors = use_safetensors
        self.pipe = None
        super().__init__()

    def generate(self, prompt: str, **kwargs):
        logger.info(f"Stable diffusion launched with the prompt of {prompt}")
        logger.info(f"Stable diffusion kwargs {kwargs}")
        self._load_pipeline()

        if not self.pipe:
            logger.exception("The pipeline has not been loaded!")
            return

    def _load_pipeline(self) -> StableDiffusionPipeline:
        logger.info(
            f"Loading StableDiffusionPipeline with the model id of {self.model_id}"
        )
        self.pipe = StableDiffusionPipeline.from_pretrained(
            self.model_id,
            use_safetensors=self.use_safetensors,
        )

        self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
            self.pipe.scheduler.config
        )

    def _load_refiner(self) -> StableDiffusionPipeline:
        pass
