import image_gen as ig
import video_editing as ve
import random
image_duration = 1.5
images = 15

ig.clear_prev_files(images)
category = input("catergory for the sad cat story (examples: beach trip, school, under the sea):\n")
ig.request_images(images, category)
songs = ("./audios/cat_ringtone.mp3", "./audios/unstoppable.mp3", "./audios/what_was_i_made_for.mp3")
song = random.choice(songs)
ve.edit(image_duration, song, images)


