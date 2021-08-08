from flask import Flask, render_template, request, jsonify
import voice, datetime, os, cfg_dev
import api_trello as api
from diana import split_word_task
from deadline import deadline

app = Flask(__name__, static_folder="static_dir")
app.config['UPLOAD_FOLDER'] = 'files/'

members_username = {
	"Иванов": "feb62",
	"Эпитов": "user07509173",
	"Малютин": 0,
}

def _trello(message):
	# -------Запись на трелку------
	now = datetime.datetime.now() # Текущее время
	task = split_word_task(message)

	idList = api.getIdList(IdBoard = os.environ["BoardID"])
	members = api.getMembers(IdBoard = os.environ["BoardID"])
	try:
		id_user = [i["id"] for i in members if i["username"] == members_username[task[0]]] # Получение ID пользователя исходя из фамилии

		card = api.newCard(name=task[1][0], IdList=idList[0]["id"], date_start=now, date_last=now+datetime.timedelta(days=30) if task[1][1] is None else deadline(now, task[1][1]), members=[ id_user ])

		answer = ["Задача была сохранена!",card['shortUrl']]
	except Exception as e:
		card = api.newCard(name=task[1][0], IdList=idList[0]["id"], date_start=now, date_last=now+datetime.timedelta(days=30) if task[1][1] is None else deadline(now, task[1][1]))
		answer = ["Задача была сохранена!",card['shortUrl'],"Warning: не был соблюдён требуемый шаблон"]
	return answer
	# -----------------------------


@app.route('/', methods=['get'])
def index():
	message = ''; file_name = ''; answer = '';
	return render_template('index.html', message=message, fn=file_name, answer_server=answer)

@app.route('/recorder', methods=['post'])
def voice_recorder():
	message = ''; file_name = ''; answer = '';
	if request.method == 'POST':
		f = request.files['file']
		if f.filename == "blob":
			file_name = f'static_dir/files/{str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))}.ogg'
		else:
			file_name = f'static_dir/files/{str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))}.{f.filename.split(".")[1]}'

		f.save(file_name)
		message, file_name, answer = voice.voice_to_text(file_name)
		if not answer: answer = _trello(message)
	return jsonify({"message":message, "fn":file_name, "answer_server":answer})

@app.route('/test', methods=['post'])
def test():
	return jsonify({"message":"Привет"})


if __name__ == "__main__":
	app.run()