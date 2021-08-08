import speech_recognition as sr
import subprocess, os

def convert_audio(audio_input, audio_output):
	os.system(f"ffmpeg -i {audio_input} {audio_output}")
	return True

def voice_to_text(name_file):
	_file = name_file.split('.')
	name_file_output = _file[0]+".wav"
	anw = convert_audio(audio_input=name_file, audio_output=name_file_output)
	try:
		if anw:
			recog = sr.Recognizer()
			sample_audio = sr.AudioFile(name_file_output)
			with sample_audio as audio_file:
				audio_content = recog.record(audio_file)
			text = recog.recognize_google(audio_content, language = "ru-RU")
			os.remove(name_file) # удаление временного аудио-файла
			answer = False
		else:
			text = False
			answer  = "Неизвестная ошибка!"
	except sr.UnknownValueError:
		text = False
		answer = "Ошибка! Звуковая дорожка пустая!"
		os.remove(name_file_output) # удаление временного аудио-файла
		
	return text, name_file_output, answer

