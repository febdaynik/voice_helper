def split_word_task(word):
	words = [
		"выполняют задание", 
		"выполняет задание",
		"делает задание", 
		"задание"
	] 
	dedline = [
		"dadlani до",
		"дедлайн до",
		"дедлайн",
		"завершить до", 
		"закончить до", 
		"сделать до",
		"закончить", 
		"завершить",
		"до"
	]
	for task_word in words:
		print("TASK WORD:",word.split(task_word).__len__() > 1, word.split(task_word))
		if word.split(task_word).__len__() > 1:
			task = [i.strip() for i in word.split(task_word)]; break

	for dedline_word in dedline:
		if task[1].split(dedline_word).__len__()>1:
			return task[0],[i.strip() for i in task[1].split(dedline_word)]
	else:
		task[1] = [task[1],None]
		return task

# GOOD:
# a = split_word_task("Иванов делает задание покушать сделать до 21 апреля")
# a = split_word_task("Иванов делает задание покушать")

# BAD:
# a = split_word_task("Иванов сделать до 21 апреля задание построить дом")


def req_punctuation():
	import random, string, requests
	from requests import Session, Request
	from requests_toolbelt import MultipartEncoder

	text = "Иванов выполняет задание покрасить дом дедлайн А Сидоров выполняет задание покушать за столом дедлайн до 1 сентября"
	fields = {
		"text":text,
		"period":"1",
	}
	boundary = '----WebKitFormBoundary' \
			   + ''.join(random.sample(string.ascii_letters + string.digits, 16))
	m = MultipartEncoder(fields=fields, boundary=boundary)

	headers={
		"Content-Type": m.content_type,
		"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.787 Yowser/2.5 Safari/537.36",
		"Cookie": f"_pk_id.25.e9f9=50f203eaf48b32e8.1630260398.; _gcl_au=1.1.279036643.1630260399; _ym_uid=1630260399365170098; _ym_d=1630260399; _ga=GA1.2.465174954.1630260400; _gid=GA1.2.1484918036.1630349336; _pk_ses.25.e9f9=1; _ym_isad=1; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IlZPUXZQWE8vcTdVekw3aFRLdk5BL2c9PSIsInZhbHVlIjoiVEJqU2RzNE5VVFh2bGV3MVV5SVA1QjNLazhPb0tQbC96L1lycFRnQkhRRW13WDM0d0hQajNlQ2xBTjhsZDc2WW0zOG1yVzB1KzhtRVJIMk5Wd1dhbk5NSE5BZ3hIL2tDdmdNSk1sbk1WbVJiQ3YyRFNrWUVmVGxkbkNYT0VBTlEiLCJtYWMiOiJkZjNjNzEyNmY2MzU1ZjllNzllMWJhOWJmYzE1MjYyNTJhNGM2YWVkYmMxNjIzNzQxZTUxY2JkYjQ1YTU3NjgzIn0%3D; tekstovod_session=eyJpdiI6IjBWZmwrRDJZZ1NTZ3VlN1l4Q0pZUGc9PSIsInZhbHVlIjoib2N6VVVycUVGMmRhajZOSFBQMlV6ZWMyN01TdzM1a3RseTlBc1F0bkdqQVFRMUlxdlZ3eWtJSEduWTMrSGZQVHFLNVFQdkJndkRpRzlqWjVlVzdIN01GdWZTZUpIRXhhN3Mwa3BwdEVRVlJtQ3RkdERlWks0Q0YzZEJWaWtuVkMiLCJtYWMiOiIwYjlmZDFlOTczY2YxYWRmZTlhNjQyYTQ0MjUxNzYyN2JkMmUzMGY2YWYwMjQ0YjVhYzYyNTAzZGZkYzUyZDEwIn0%3D",
		"X-XSRF-TOKEN": "eyJpdiI6IlZPUXZQWE8vcTdVekw3aFRLdk5BL2c9PSIsInZhbHVlIjoiVEJqU2RzNE5VVFh2bGV3MVV5SVA1QjNLazhPb0tQbC96L1lycFRnQkhRRW13WDM0d0hQajNlQ2xBTjhsZDc2WW0zOG1yVzB1KzhtRVJIMk5Wd1dhbk5NSE5BZ3hIL2tDdmdNSk1sbk1WbVJiQ3YyRFNrWUVmVGxkbkNYT0VBTlEiLCJtYWMiOiJkZjNjNzEyNmY2MzU1ZjllNzllMWJhOWJmYzE1MjYyNTJhNGM2YWVkYmMxNjIzNzQxZTUxY2JkYjQ1YTU3NjgzIn0="
	}
	req = requests.post("https://textovod.com/punctuation", data=m, headers=headers)

	return req.json()

print(req_punctuation())