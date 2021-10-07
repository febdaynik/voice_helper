import speech_recognition as sr
import subprocess, os
import random, string

def convert_audio(audio_input, audio_output):
	os.system(f"ffmpeg -i {audio_input} {audio_output}")
	return True

def voice_to_text(name_file):
	_file = name_file.split('.')
	if _file[1] != "wav":
		name_file_output = _file[0]+".wav"
		anw = convert_audio(audio_input=name_file, audio_output=name_file_output)
	else:
		anw = True; name_file_output = name_file; 
	try:
		if anw:
			recog = sr.Recognizer()
			sample_audio = sr.AudioFile(name_file_output)
			with sample_audio as audio_file:
				audio_content = recog.record(audio_file)
			text = recog.recognize_google(audio_content, language = "ru-RU")
			# os.remove(name_file) # удаление временного аудио-файла
			answer = False
		else:
			text = False
			answer  = "Неизвестная ошибка!"
	except sr.UnknownValueError:
		text = False
		answer = "Ошибка! Звуковая дорожка пустая!"
		os.remove(name_file_output) # удаление временного аудио-файла
		
	return text, name_file_output, answer

class FinderVoice:
	def __init__(self, text):
		self.trigger_surname = ["Иванов","Сидоров","Малютин","Эпитов"]
		self.trigger_deadline =[
			"dadlani до",
			"дедлайн до",
			"дедлайн",
			"завершить до", 
			"закончить до", 
			"сделать до",
			"закончить", 
			"завершить",
			"до",
			"выполнить к",
			"сделать к",
			"закончить к"
		]
		self.trigger_word_task = [
			"выполняют задание", 
			"выполняет задание",
			"делает задание", 
			"задание",
			"назначен по заданию",
			"цель",
			"назначить задачу",
			"назначить"		] 
		self.text = text.split(".")
		self.surname_in_text = []
		self.find_arr_surname = []
		self.arr_text_task = []
		self.arr_deadline_task = []

	def find_surname_in_text(self):
		for value in self.text:
			for surname in self.trigger_surname:
				if value.strip().find(surname) != -1:
					self.surname_in_text.append(value)
					self.find_arr_surname.append(surname)

		return self.find_text_task()

	def find_text_task(self):
		for index,word in enumerate(self.surname_in_text):

			for task_word in self.trigger_word_task:
				if word.split(task_word).__len__() > 1:
					task = [i.strip() for i in word.split(task_word)] 
					task_text, text_deadline = self.split_no_task(task, index)
					self.arr_text_task.append(task_text)
					self.arr_deadline_task.append(text_deadline)
					break

		return [self.find_arr_surname, self.arr_text_task, self.arr_deadline_task]

	def split_no_task(self, tasks, index):
		for tw in tasks:
			if tw.find(self.find_arr_surname[index]) == -1:
				return self.split_deadline(tw)

	def split_deadline(self, task_text):
		for dedline_word in self.trigger_deadline:
			if task_text.split(dedline_word).__len__()>1:
				return [i.strip() for i in task_text.split(dedline_word)]
		else:
			return [task_text, None]


def dot_in_text(text):
	new_text = ""
	for c in text:
		if c.isupper():
			new_text += "."
		new_text += c
	return new_text
	
if __name__ == '__main__':
	pass
	# text = voice_to_text("static_dir/files/20210919151337852533.wav")[0]
	text = "Иванов выполняет задание покрасить дом Сидоров выполняет задание покушать за столом дедлайн до 1 сентября"
	text = dot_in_text(text)

	# bot = FinderVoice(text=text)
	# fsit = bot.find_surname_in_text()
	# print(fsit)
	import test_trello
	answer = test_trello.main(text)
	print(answer)
