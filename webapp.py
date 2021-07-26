from flask import Flask, render_template, request
import voice 
import datetime
import os
import api_trello as api

app = Flask(__name__, static_folder="static_dir") # приложение фласка
app.config['UPLOAD_FOLDER'] = 'files/'


members_username = {
	"Иванов": "feb62",
	"Эпитов": 0,
	"Малютин": 0,
}


def split_task(word):
	# task_word = ["задание", "задания"] # удалить
	# task_word = ["выполняет задание", "выполняет задания"] # удалить
	arr = word.split("выполняет задание")
	return [i.strip() for i in arr]


@app.route('/', methods=['post', 'get'])
def index():
	message = ''; file_name = ''; answer = '';
	if request.method == 'POST':
		f = request.files['file']

		file_name = 'static_dir/files/{}.wav'.format(str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")))
		f.save(file_name)
		message = voice.voice_to_text(file_name)

		# -------Запись на трелку------
		now = datetime.datetime.now() # Текущее время
		task = split_task(message) # Выделяем имя и задачу в тексте

		idList = api.getIdList(IdBoard = "60d0646f90d48645032c4820")
		members = api.getMembers(IdBoard = "60d0646f90d48645032c4820")
		id_user = [i["id"] for i in members if i["username"] == members_username[task[0]]] # Получение ID пользователя исходя из фамилии

		
		card = api.newCard(name=task[1], IdList=idList[0]["id"], date_start=now, date_last=now+datetime.timedelta(days=30), members=[ id_user ])
		answer = ["Задача была сохранена!",card['shortUrl']]
		# -----------------------------

		# os.remove(file_name) # удаление временного аудио-файла
	print(file_name)
	return render_template('index.html', message=message, fn=file_name, answer_server=answer)
	
if __name__ == "__main__":
	app.run()