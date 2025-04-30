import base64
import os

base_dir = os.path.dirname(os.path.abspath(__file__))  
image_path = os.path.join(base_dir, "..", "assets", "images", "noImage.jpg")  


def image_to_base64(image_path: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

