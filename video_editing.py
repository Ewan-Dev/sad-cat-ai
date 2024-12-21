from PIL import Image
import random
import math
import os
from moviepy.editor import *
def edit(secs, audio, image_num, video_path):
    image_clip = []
    for i in range(image_num - 1):
        path= f"./images/image{i}.png"
        image_exists = os.path.exists(path)
        if image_exists:
            print(f"{path} exists")
            image_clip.append(ImageClip(path).set_duration(secs))
    image_slideshow = concatenate(image_clip, method="compose")
    slideshow_duration = math.floor(image_slideshow.duration)
    audio_clip = AudioFileClip(audio)
    audio_duration = math.floor(audio_clip.duration)
    end_time = min(slideshow_duration, audio_duration)
    image_slideshow.audio = audio_clip.subclip(0, end_time)
    watermarkemoji1 = TextClip("4(", fontsize= 80, font="./fonts/GumiFontSymbols-Regular.ttf", stroke_width=6, color="white").set_position((100, 800)).set_duration(slideshow_duration).set_opacity(0.5)
    watermark = TextClip("@lucky.catstory", fontsize=80, color="#fff", stroke_width=3, font="./fonts/CherryBombOne-Regular.ttf").set_position((300, 800)).set_duration(slideshow_duration).set_opacity(0.5)
    text1 = TextClip("follow and comment heart emoji ♡", fontsize=75, stroke_width=6, stroke_color="#38659c", color="#b3daff", font="./fonts/CherryBombOne-Regular.ttf").set_position((45, 70)).set_duration(slideshow_duration).set_opacity(0.5)
    text2 = TextClip("if you love animals", fontsize=75, stroke_width=6, stroke_color="#38659c", color="#b3daff", font="./fonts/CherryBombOne-Regular.ttf").set_position((65, 170)).set_duration(slideshow_duration).set_opacity(0.5)
    image_slideshow = CompositeVideoClip([image_slideshow, text1, text2, watermarkemoji1, watermark])

    image_slideshow.write_videofile(video_path, fps=24)
    