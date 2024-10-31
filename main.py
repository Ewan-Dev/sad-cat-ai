import image_gen as ig
import video_editing as ve
import random
import title_gen as tg
import video_upload as vu 

#YOUR GOOGLE LOGIN
username = ''
password = ''

#CHANNEL URL EXAMPLE: https://www.youtube.com/channel/UCGuFWvnSolLc706mc17JkDQ 
channel_url = ''

image_duration = 1.5 #seconds
images = 15

repeats = input("video amount:")
ask_catergory = input("prompt for catergory after each initisation? y/N")

if ask_catergory == "y":
    repeats_num = int(repeats)
    for i in range(repeats_num):
        file = f"./final{i}.mp4"
        category = input("catergory for the sad cat story (examples: beach trip, school, under the sea):\n")
        ig.clear_prev_files(images)
        story = ig.request_story(images, category)
        ig.request_images(story)
        songs = ("./audios/cat_ringtone.mp3", "./audios/unstoppable.mp3", "./audios/what_was_i_made_for.mp3")
        song = random.choice(songs)
        ve.edit(image_duration, song, images)
        name = tg.get_title(story)
        vu.upload(file, name)

if ask_catergory == "N":
    category = "a sad cat story with a strong plot for example- getting stranded off boat and needing to set up shelter and fie and food anther example- cat parents need to commit crimes to feed kittens- another inspiration- cat is bullied at school so he plots revenge as his feeings are hurt- another- cat has terminal illness and dies- another- end of cat planet world id coming " #if the user does not input the LLM will pick a random topic
    for i in range(repeats):
        file = f"./final{i}.mp4"
        ig.clear_prev_files(images)
        story = ig.request_story(images, category)
        ig.request_images(story)
        songs = ("./audios/cat_ringtone.mp3", "./audios/unstoppable.mp3", "./audios/what_was_i_made_for.mp3")
        song = random.choice(songs)
        ve.edit(image_duration, song, images)
        name = tg.get_title(story)
        vu.upload(file, name, username, password, channel_url)



