import torch, json
from diffusers import PixArtAlphaPipeline

def generate_image():
    DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

    pipe = PixArtAlphaPipeline.from_pretrained("PixArt-alpha/PixArt-XL-2-1024-MS", torch_dtype=torch.float16)
    pipe = pipe.to(DEVICE)

    with open(r'.\\info\\user_info\\user_info.json', 'r') as json_file:
        data = json.load(json_file)

    prompt = f'Generate an image with resolution (200*350) strictly of a person with attributes: {data}"'
    result = pipe(prompt).images[0]

    image_path = 'static/images/user.png'

    result.save(image_path)