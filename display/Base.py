from display.Window import *
from ttkbootstrap import *
import ttkbootstrap as tbs
from PIL import ImageTk, Image

frame = getFrame()

def createButton(text, event, pady):
    tbs.Button(frame, text=text, command=event).pack(pady=pady)

def drawText(text, font, pady):
    tbs.Label(frame, text=text, font=font, bootstyle="default").pack(pady=pady)

def drawImage(image, pady):
    global imageSrc
    imageSrc = Image.open(image)
    imageSrc = ImageTk.PhotoImage(imageSrc)
    tbs.Label(frame, image=imageSrc).pack(pady=pady)
