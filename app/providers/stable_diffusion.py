import torch
from diffusers import DPMSolverMultistepScheduler, StableDiffusionPipeline

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
        self.low_cpu_memory_usage = True
        self.is_cuda_available = torch.cuda.is_available()
        self.torch_type = torch.float32
        self.pipe = None

        super().__init__()

    @property
    def device(self):
        return "cuda" if self.is_cuda_available else "cpu"

    def generate(self, prompt: str, **kwargs):
        logger.info(f"Stable diffusion launched with the prompt of {prompt}")
        logger.info(f"Stable diffusion kwargs {kwargs}")

        self._load_pipeline()

        if not self.pipe:
            logger.exception("The pipeline has not been loaded!")
            raise RuntimeError("The pipeline has not been initialized!")

        negative_prompt = kwargs.get(
            "negative_prompt",
            "disfigured, low quality, text, ugly",
        )

        height = kwargs.get("height", 768)
        width = kwargs.get("width", 768)
        high_noise_frac = kwargs.get("high_noise_frac", 0.8)
        num_inference_steps = kwargs.get("num_inference_steps", 25)
        num_images_per_prompt = kwargs.get("num_images_per_prompt", 2)

        result = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            height=height,
            width=width,
            denoising_end=high_noise_frac,
            num_inference_steps=num_inference_steps,
            num_images_per_prompt=num_images_per_prompt,
        )

        return result

    def _load_pipeline(self):
        logger.info(
            f"Loading StableDiffusionPipeline with the model id of {self.model_id}"
        )

        try:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                self.model_id,
                torch_dtype=self.torch_type,
                low_cpu_mem_usage=self.low_cpu_memory_usage,
                use_safetensors=self.use_safetensors,
            )
        except Exception as e:
            logger.exception(f"Error loading StableDiffusionPipeline: {e}")
            raise

        try:
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipe.scheduler.config
            )
        except Exception as e:
            logger.error(f"Error setting scheduler: {e}")

        try:
            self.pipe.to(self.device)
        except Exception as e:
            logger.error(f"Error moving pipeline to device {self.device}: {e}")

        logger.info("Stable Diffusion pipeline has been loaded!")
