import requests


def get_title(story):
    base_url = "https://text.pollinations.ai/prompt/"
    title = ["papa steal food for starving kitty #cat #cute #citten #trending #catlover #cutecat #shorts", "Koala 🆚 leopard, revenge for fathe😭😭, #cat #cute #citten #trending #catlover #cutecat #shorts", "Cat Sad Real Story #kitten #cat #aicat #catlovers#cutekitten #catvideos #catshorts#cutecatstories", "Kitty Cat Angry Neighbour😿#shorts #cat #cute #kitten #funny #sadcat #poorcat #ai #kittycat #aicat", "Poor Cats have wings like butterflies. 😱 mermaid kitten 😿❤️ #cat #ai #aicat #catlover #貓", "He learned a lesson 😿 #cat #cutecat #catmemes #sad #story #inspiration #aiimages #chatgpt4 #ai", "Ai Cat Kidnep Sad Story #viral #cuteanimal #catlover #cutecat #cat #youtubeshorts", "What u do if phone drops in toilet?#cat #cute #kitten #funny #catlover #kitty"],
    messages = "Make a simple youtube video title less than 6 words and put 3 tags with octothorpes before do to with ai cats characters for the story and take heavy inspiration from sucessful titles in the titles list as they were very sucessful, including emojis and tags and no grammar at all and return it as plain text and refer to the cat's name as just the word cat nothing else and RETURN IN PLAIN TEXT WITHOUT LABELS OR MARKDOWN ANNOTATIONS"
    response = requests.get(f"{base_url}{messages}{story}titles-list:{title}")
    title = response.text
    if response.status_code == 200:
        print(title)
        #returns correct ai genereated title
        return title
    else:
        # returns default title
        print("failed to generate title")
        return "sadcat story #aicat #trending #cat #cute #sadcat #sadstory #aicat #catlover #kitten"    
