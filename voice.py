import speech_recognition as sr
from pydub import AudioSegment
import os

def voice_to_text(name_file):
	recog = sr.Recognizer()
	try:
		sample_audio = sr.AudioFile(name_file)
		with sample_audio as audio_file:
			audio_content = recog.record(audio_file)
		text = recog.recognize_google(audio_content, language = "ru-RU")
		return text, name_file
	except ValueError as e:
		_file = name_file.split('.')
		if _file[1] == "mp3":
			sound = AudioSegment.from_mp3(file=name_file)
		elif _file[1] == "flv":
			sound = AudioSegment.from_flv(file=name_file)
		elif _file[1] == "ogg":
			sound = AudioSegment.from_ogg(file=name_file)
		elif _file[1] == "raw":
			sound = AudioSegment.from_raw(file=name_file)

		os.remove(name_file) # удаление временного аудио-файла
		sound.export(_file[0]+".wav", format="wav")
		return voice_to_text(_file[0]+".wav")

