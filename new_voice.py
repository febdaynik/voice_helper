import speech_recognition as sr
import os
import requests, json

text = "Хорошо я тебя понял тогда я могу тебе сказать о том что Иванов выполняет задание отремонтировать машину А ещё что можно сказать я могу тебе ещё сказать что Сидоров выполняет задание погулять с собакой"



# def split_surname(text):
# 	arr = []
# 	for surname in surname_list:
# 		if text.split(surname).__len__() > 1:
# 			arr.append(text.split(surname)[1])
# 	print(arr)

# split_surname(text)
# text = {i for i in text.split()}

# <mark onclick="$(this).remove();">,</mark>

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
			"выполнить к"
		]
		self.trigger_word_task = [
			"выполняют задание", 
			"выполняет задание",
			"делает задание", 
			"задание",
			"назначен по заданию",
			"цель",
			"назначить задачу",
			"назначить"
		] 
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
					task_text,text_deadline = self.split_no_task(task, index)
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
		# else:
			# task[1] = [task[1],None]
			# return task

# bot = FinderVoice(text=text)
# bot.find_surname()

# import random, string
# from requests_toolbelt import MultipartEncoder
# text ='Иванов выполняет задание погулять с собакой дедлайн до 25 марта Но Сидоров выполняет задание отремонтировать машину дедлайн до 7 февраля'
# text = "Короче<mark onclick=\"$(this).remove();\">,</mark> надо мне записать сейчас какой-то голосовую<mark onclick=\"$(this).remove();\">,</mark> который будет 3 рэп<mark onclick=\"$(this).remove();\">,</mark> специальным<mark onclick=\"$(this).remove();\">,</mark> который мне потребуется для составления системы б**** мешаешь<mark onclick=\"$(this).remove();\">.</mark> В общем<mark onclick=\"$(this).remove();\">,</mark> Иванов выполняет задание покрасить дом<mark onclick=\"$(this).remove();\">.</mark> также надо не забывать<mark onclick=\"$(this).remove();\">,</mark> что Сидоров выполняет задание покушать за столом"
text = "Иванов выполняет задание покрасить дом дедлайн. А Сидоров выполняет задание покушать за столом дедлайн до 1 сентября"
text = text.replace('<mark onclick="$(this).remove();">.</mark>', ".").replace('<mark onclick="$(this).remove();">,</mark>', "")
# print(text)


# fields = {
# 	"text":text,
# 	"period":"1",
# }
# boundary = '----WebKitFormBoundary' \
# 		   + ''.join(random.sample(string.ascii_letters + string.digits, 16))
# m = MultipartEncoder(fields=fields, boundary=boundary)

# headers={
# 	"Content-Type": m.content_type,
# 	"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.787 Yowser/2.5 Safari/537.36",
# 	"Cookie": "_pk_id.25.e9f9=9b35b7de79468fd0.1629374107.; _pk_ref.25.e9f9=%5B%22%22%2C%22%22%2C1629374107%2C%22https%3A%2F%2Fyandex.ru%2F%22%5D; _pk_ses.25.e9f9=1; _ym_uid=1629374107657576478; _ym_d=1629374107; __gads=ID=4aa2f8e6774c5fc6-22ecb4eba5c800d6:T=1629374109:RT=1629374109:S=ALNI_MYGitRxRDFt89HdNamTiJxKDpzpsw; _ym_visorc=w; _gcl_au=1.1.587812965.1629374108; _ga=GA1.2.1400065373.1629374106; _gid=GA1.2.1916520190.1629374110; _ym_isad=2; XSRF-TOKEN=eyJpdiI6IjZ5Y2dmS1lySUR5R0huU0VVU0QzZ3c9PSIsInZhbHVlIjoiaHY4ZXpZVElVTG4veUF0Q3laUld4cnVXbWQ0cGdoTStuWnNValRJSGRTVEhUc2d2akhlY2l6cGQ4UmtUUmRGcC9JN0I0V3N2d3hYMHUxZk10TGl1TlZHVHVWVndWdmhJdlVEOWFramVLZWUvaTZQM3BLa3VkKzdzTHFqME91cEIiLCJtYWMiOiI5NGIzNDZlZmFlNzMzNGQxYTMwNTY3YzFmZWU4NTljYzM4YjVmNTRlNmU1NDI3Njc1NjIxNzAzZDNjYzEzNWRlIn0%3D; tekstovod_session=eyJpdiI6IjBBVFFsb2VtVWtMbGsyclFjb1NaeHc9PSIsInZhbHVlIjoiNllNMHBCK0VOUUJsQzFYUFVFYklWSzJ1bWJiR0l2WlZtZldHOEtjaHdZQXJib0tOWFNETG94bEFRd3ZuV1NrQ0Y4MnE0ZEdkR3VRL0EzWGx3VEhFYkVuSDQwUlZqaDNETVRGb1NUUkJUUEsvU290Tm1KYkp1clZZcTdpejRJNFUiLCJtYWMiOiJmOWQ4YmI5ZGRmNWJlYWRmMWE4NTk1NzJlMjYxZTU4ZWVjNDVjM2EwNDRmODFkYjhjN2ZmYzM0ZjI3OWUyMDliIn0%3D",
# 	"X-XSRF-TOKEN": "eyJpdiI6IjZ5Y2dmS1lySUR5R0huU0VVU0QzZ3c9PSIsInZhbHVlIjoiaHY4ZXpZVElVTG4veUF0Q3laUld4cnVXbWQ0cGdoTStuWnNValRJSGRTVEhUc2d2akhlY2l6cGQ4UmtUUmRGcC9JN0I0V3N2d3hYMHUxZk10TGl1TlZHVHVWVndWdmhJdlVEOWFramVLZWUvaTZQM3BLa3VkKzdzTHFqME91cEIiLCJtYWMiOiI5NGIzNDZlZmFlNzMzNGQxYTMwNTY3YzFmZWU4NTljYzM4YjVmNTRlNmU1NDI3Njc1NjIxNzAzZDNjYzEzNWRlIn0="
# }

# req = requests.post('https://textovod.com/punctuation', headers=headers, data=m)
# print(req.json())
if __name__ == '__main__':
	# text = 'Хорошо<mark onclick="$(this).remove();">,</mark> я тебя понял<mark onclick="$(this).remove();">.</mark> тогда я могу тебе сказать о том<mark onclick="$(this).remove();">,</mark> что Иванов выполняет задание<mark onclick="$(this).remove();">,</mark> отремонтировать машину<mark onclick="$(this).remove();">.</mark> А ещё что можно сказать<mark onclick="$(this).remove();">.</mark> я могу тебе ещё сказать<mark onclick="$(this).remove();">,</mark> что Сидоров выполняет задание погулять с собакой<mark onclick="$(this).remove();">.</mark>'
	# print(text.split('<mark onclick="$(this).remove();">.</mark>')[0])
	# text = text.replace('<mark onclick="$(this).remove();">.</mark>', ".").replace('<mark onclick="$(this).remove();">,</mark>', "")
	# text = text.replace('<mark onclick="$(this).remove();">,</mark>', ",")
	# print(text.split('.'))

	def finder(text):
		arr = []
		for t in text.split("."):
			for i in ["Иванов","Сидоров","Малютин","Эпитов"]:
				if t.strip().find(i) != -1: 
					arr.append(t.strip())
				# print() 

		for i in arr:
			print(i.split())
		# print(arr)
	# finder(text)
	bot = FinderVoice(text=text)
	a = bot.find_surname_in_text()
	print(a)

