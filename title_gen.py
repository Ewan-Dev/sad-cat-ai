import requests


def get_title(story):
    base_url = "https://text.pollinations.ai/prompt/"
    title = ["papa steal food for starving kitty #cat #cute #citten #trending #catlover #cutecat #shorts", "Koala 🆚 leopard, revenge for fathe😭😭, #cat #cute #citten #trending #catlover #cutecat #shorts", "Cat Sad Real Story #kitten #cat #aicat #catlovers#cutekitten #catvideos #catshorts#cutecatstories", "Kitty Cat Angry Neighbour😿#shorts #cat #cute #kitten #funny #sadcat #poorcat #ai #kittycat #aicat", "Poor Cats have wings like butterflies. 😱 mermaid kitten 😿❤️ #cat #ai #aicat #catlover #貓", "He learned a lesson 😿 #cat #cutecat #catmemes #sad #story #inspiration #aiimages #chatgpt4 #ai", "Ai Cat Kidnep Sad Story #viral #cuteanimal #catlover #cutecat #cat #youtubeshorts", "What u do if phone drops in toilet?#cat #cute #kitten #funny #catlover #kitty"],
    messages = "Make a Youtube video title less than 60 characters for the story and take heavy inspiration from sucessful titles in the titles list as they were very sucessful, including emojis and tags and no grammar and return it as plain text and efer to the cats as just cat"
    response = requests.get(f"{base_url}{messages}{story}titles-list:{title}")
    title = response.text
    if response.status_code == 200:
        print(title)
        #returns correct ai genereated title
        return title
    else:
        # returns default title
        print("fial")
        return "sadcat story #aicat #trending #cat #cute #sadcat #sadstory #aicat #catlover #kitten"    
