import requests
import random
import os
import shutil
from PIL import Image
from io import BytesIO

base_url_story = "https://text.pollinations.ai"
base_url_image = "https://image.pollinations.ai/prompt"

def clear_prev_files(x):
    image_path = "./images"

    if os.path.exists(image_path):
        shutil.rmtree(f"{image_path}")
        print(f"removed:{image_path}")
    else:
            print(f"{image_path} does not exist so it couldn't be removed")
    if os.path.exists("final.mp4"):
            os.remove("final.mp4")
            print(f"removed:final.mp4")
    else:
            print(f"final.mp4 does not exist so it couldn't be removed")
    os.mkdir("images")
    return 1

def get_prompt_story(prompt):
    url = f"{base_url_story}/{prompt}make-sure-the-cat-is-in-every-scene-"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to get story prompt {response.status_code}")

def get_prompt_images(prompt, index):
    url = f"{base_url_image}/{prompt}-the-cat-is-ginger-the-extremely-exaggerated-emotion--real-8k-realistic-3d?width=1080&height=1920" #random number to avoid same api call leading to same images from pollinations""
    response = requests.get(url)
    if response.status_code == 200:
        image = ''
        image = Image.open(BytesIO(response.content))
        image.save(f"./images/image{index}.png")
        image.show()
    else:
        print(f"Failed to get image {index}")


def request_images(number, subject):
    request_number = random.randint(1,1000000)
    prompt = f"Write-a-very-sad-and-emotional-catstory-with-only-{number}-sentences-and-its-about-{subject}of-a-ginger-cat-who-appears-in-every-scene-capable-of-human-like-actions-Each-sentence-should-feel-like-an-image-description-like-of-a-comic-book-avoiding-close-ups-and-pronouns-to-refer-to-the-cats-but-instead-use-their-appearance-to-refer-to-them-and-keeping-the-setting-in-view-only-{number}-sentences-request-{request_number}" #random number to avoid same api call leading to same images from pollinations
    prompt_story = get_prompt_story(f"ginger-cat{prompt}")
    if prompt_story:
        story_images = []
        prompt_story = prompt_story.split(".")
        for i , x in (enumerate(prompt_story)):
            get_prompt_images(prompt_story[i], i)


