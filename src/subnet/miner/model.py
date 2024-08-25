from communex.module import Module, endpoint
from communex.key import generate_keypair
from keylimiter import TokenBucketLimiter
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch
import os


class Miner(Module):
    """
    A module class for mining and generating images based on prompts.

    Attributes:
        model: The Stable Diffusion model pipeline for image generation.

    Methods:
        generate: Generates an image based on a given prompt.
    """

    def __init__(self):
        """
        Initializes the Miner with the Stable Diffusion model pipeline.
        """
        super().__init__()
        self.model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
        self.model.to("cuda" if torch.cuda.is_available() else "cpu")

    @endpoint
    def generate(self, prompt: str):
        """
        Generates an image based on a given prompt using the Stable Diffusion model.

        Args:
            prompt: The prompt to generate an image for.

        Returns:
            image_path: The path to the generated image.
        """
        print(f"Generating image for prompt: `{prompt}`")

        # Generate the image
        image = self.model(prompt).images[0]

        # Save the image
        image_path = f"output_{prompt.replace(' ', '_')}.png"
        image.save(image_path)

        print(f"Image saved to `{image_path}`")
        return image_path


if __name__ == "__main__":
    """
    Example of running the miner module.
    """
    from communex.module.server import ModuleServer
    import uvicorn

    # Generate key pair for the miner
    key = generate_keypair()
    miner = Miner()

    # Set up a token bucket limiter
    refill_rate = 1 / 400  # Tokens are refilled at a rate of 1 token every 400 seconds
    bucket = TokenBucketLimiter(2, refill_rate)

    # Set up the module server with IP limiting and subnet whitelist
    server = ModuleServer(miner, key, ip_limiter=bucket, subnets_whitelist=[3])
    app = server.get_fastapi_app()

    # Only allow local connections
    uvicorn.run(app, host="127.0.0.1", port=8000)
