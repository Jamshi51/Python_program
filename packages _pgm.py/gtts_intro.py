from gtts import gTTS
import os
s=input("enter your text : ")
c=gTTS(text=s,lang="en",slow=False)
#c=gTTS(text=s,lang="ml",slow=False)
c.save("test_audio.mp3")
os.system("start test_audio.mp3")
