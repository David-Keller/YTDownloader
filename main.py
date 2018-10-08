import search
import video

def guiUpdateCallback():
    print("gui Updated")
    
guiUpdate = guiUpdateCallback

search = Search(guiUpdate)