# from gtts import gTTS
# import os
# s=input("enter text :")
# c=gTTS(text=s,lang="en",slow=False)
# #c=gTTS(text=s,lang="ml",slow=False)
# c.save("test_audio.mp3")
# os.system("start test_audio.mp3")


# from gtts import gTTS
# import os

# s = "hiii"

# # Create gTTS object (choose language and speed)
# c = gTTS(text=s, lang="en", slow=False)  
# # c = gTTS(text=s, lang="ml", slow=False)  # Uncomment for Malayalam

# # Save the generated speech to an mp3 file
# c.save("test_audio.mp3")

# # Play the mp3 file
# os.system("start test_audio.mp3")  # Works on Windows


from gtts import gTTS
import os

s = "-"  # The text
c = gTTS(text=s, lang="en", slow=False)  # ✅ Create gTTS object

c.save("test_audio.mp3")  # ✅ Save using gTTS object
os.system("start test_audio.mp3")  # Play the file (Windows)