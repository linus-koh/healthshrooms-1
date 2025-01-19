from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path="generated_image.png"):
    # Load the Stable Diffusion pipeline
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")  # Ensure GPU is used for faster generation

    # Generate the image
    print("Generating image. This may take a moment...")
    image = pipe(prompt).images[0]

    # Save the generated image
    image.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    generate_image(user_prompt, "output_image.png")
