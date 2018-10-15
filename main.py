import search as s
import video as v

def guiUpdateCallback():
    print("gui Updated")
    
guiUpdate = guiUpdateCallback

search = s.Search(guiUpdate)