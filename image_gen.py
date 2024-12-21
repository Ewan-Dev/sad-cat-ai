import requests
import random
import os
import shutil
from PIL import Image
from io import BytesIO

base_url_story = "https://text.pollinations.ai/"
base_url_image = "https://image.pollinations.ai/prompt/"

def clear_prev_files(x):
    image_path = "./images"
    videos_path = "./videos"
    if os.path.exists(image_path):
        shutil.rmtree(f"{image_path}")
        print(f"removed:{image_path}")
    else:
            print(f"{image_path} does not exist so it couldn't be removed")
    if os.path.exists(videos_path):
            shutil.rmtree(f"{videos_path}")
            print(f"removed:{videos_path}")
    else:
            print(f"{videos_path} does not exist so it couldn't be removed")
    os.mkdir("videos")
    os.mkdir("images")
    return 1

def get_prompt_story(prompt):
    url_v1 = f"{base_url_story}/{prompt}make-sure-the-plot-is-strong-and-emotional"
    url_v2 = f"{url_v1}-from-that-text-make-sure-every-scene-is-a-description-for-an-ai-image-gen-prompt-being-descrivetive-of-realtive-size-and-position-as-well-as-appearence"
    url_final = f"{url_v2}-eradiacate-any-use-of-pronuns-replacing-them-with-the-descrptions-instead"
    response = requests.get(url_final)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to get story prompt {response.status_code}")
        return 0

def get_prompt_images(prompt, index):
    url = f"{base_url_image}/{prompt}-the-cat-is-ginger-realistic-3d-style-the-extremely-exaggerated-emotion-real-8k-realistic-3d?width=1080&height=1920"
    
    response = requests.get(url)
    if response.status_code == 200:
        image = ''
        image = Image.open(BytesIO(response.content))
        image.save(f"./images/image{index}.png")
        return 1
    else:
        print(f"Failed to get image {index}")
        return 0

def request_story(number, subject):
    request_number = random.randint(1,1000000)
    prompt = f"Write-a-very-sad-heart-wrenching-cryable-and-emotional-catstory-with-only-{number}-sentences-and-its-about-{subject}of-a-ginger-cat-is-capable-of-human-like-actions-keeping-the-setting-in-view-only-{number}-sentences-and-all-cats-have-clothes-that-are-a-part-of-their-charcter-so-make-sure-you-tell-us-the-cats-clothing-in-the-descriptions-++request-{request_number}" #random number to avoid same api call leading to same images from pollinations
    prompt_story = get_prompt_story(prompt)
    return prompt_story

def request_images(story):
    if story:
        story_images = []
        story = story.split(".")
        for i , x in (enumerate(story)):
            get_prompt_images(story[i], i)
    return 1

