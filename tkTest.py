# these two commands need to be run inorder for this to work on linux work machines:
#sudo apt-get install python3-pil python3-pil.imagetk
#sudo apt-get install python3-tk

import tkinter as tk

# used to make jpg and other image formats compatable with tkinter
from PIL import Image, ImageTk
#used to download image data
import requests
from io import BytesIO


url = "https://i.ytimg.com/vi/uLHYfJZPQjo/default.jpg"

root = tk.Tk()

# download the thumbnail image and save it to ram
response = requests.get(url)
tkimage = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))

tk.Label(root, image=tkimage).pack()
root.mainloop()