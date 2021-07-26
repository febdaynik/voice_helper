import speech_recognition as sr

def voice_to_text(name_file):
	recog = sr.Recognizer()
	sample_audio = sr.AudioFile(name_file)
	with sample_audio as audio_file:
		audio_content = recog.record(audio_file)
	text = recog.recognize_google(audio_content, language = "ru-RU")
	return text

if __name__ == '__main__':
	print(voice_to_text("test.wav"))