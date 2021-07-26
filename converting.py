import os
from pydub import AudioSegment

# sound = AudioSegment.from_wav("test.wav")
# sound.export("123.mp3", format="mp3")

# convert wav to mp3
sound = AudioSegment.from_mp3(file=os.path.abspath("123.mp3"))
sound.export("test.wav", format="wav")

# print()