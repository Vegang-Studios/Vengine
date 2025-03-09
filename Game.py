from display.Base import *
from misc.Json import *

setTitle(getGameTitle())
setSize(300, 150)
resizable(False)

clicks = 0

def clicked():
        drawText("Tu as cliqué !", ("Fredoka", 15), 15)

createButton("Clique !", clicked, 15)

runningLoop()