from PIL import Image
import pywhatkit


Image.open('wolves.png')
pywhatkit.image_to_ascii_art('wolves.png', 'MyArt')
read_file = open("MyArt.txt", "r")
print(read_file.read())

