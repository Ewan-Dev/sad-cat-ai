import image_gen as ig
import video_editing as ve
import random
import title_gen as tg
import video_upload as vu 
from flask import Flask, redirect, url_for, render_template, request

#YOUR GOOGLE LOGIN
username = ''
password = ''

#CHANNEL URL EXAMPLE: https://studio.youtube.com/channel/UCGuFWvnSolLc706mc17JkDQ
channel_url = ''
image_duration = 1.5 #seconds
images = 15

repeats = ''
category = "a sad cat story with a strong plot for example- getting stranded off boat and needing to set up shelter and fie and food anther example- cat parents need to commit crimes to feed kittens- another inspiration- cat is bullied at school so he plots revenge as his feeings are hurt- another- cat has terminal illness and dies- another- end of cat planet world id coming " #if the user does not input the LLM will pick a random topic
video_type = ''

app = Flask(__name__, template_folder='static/templates')
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        repeats = request.form["vid-amount"]
        category = request.form["catergory"]
        video_type = request.form["vid-type"]
        main(repeats, category, video_type)
        return render_template("index.html")
    else:
        return render_template("index.html")
def main(repeats, category, video_type):
    if video_type == "story":
        repeats_num = int(repeats)
        for i in range(repeats_num):
            file = f"./videos/final{i}.mp4"
            ig.clear_prev_files(images)
            story = ig.request_story(images, category)
            ig.request_images(story)
            songs = ("./audios/cat_ringtone.mp3", "./audios/unstoppable.mp3", "./audios/what_was_i_made_for.mp3")
            song = random.choice(songs)
            ve.edit(image_duration, song, images, file)
            name = tg.get_title(story)
            vu.upload(file, name, username, password, channel_url)

if __name__ == "__main__":
    app.run(debug=True)


