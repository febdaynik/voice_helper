import cfg_dev, datetime, os
import api_trello as api
from deadline import deadline
from voice import FinderVoice

def main(text):

	members_username = {
		"Иванов": "feb62",
		"Сидоров":"nicolay63",
		"Эпитов": "user07509173",
		"Малютин": 0,
	}

	bot = FinderVoice(text=text)
	tasks = bot.find_surname_in_text()

	now = datetime.datetime.now() # Текущее время

	# -------Запись на трелку------
	idList = api.getIdList(IdBoard = os.environ["BoardID"])
	members = api.getMembers(IdBoard = os.environ["BoardID"])

	answer = ""
	for index,name_ in enumerate(tasks[0]):
		try:
			id_user = [i["id"] for i in members if i["username"] == members_username[name_]] 
			card = api.newCard(name=tasks[1][index], IdList=idList[0]["id"], date_start=now, date_last=now+datetime.timedelta(days=30)  if tasks[2][index] is None else deadline(now, task[2][index]), members=[ id_user ])
			answer = f"Задача №{index+1} для {name_} добавлена"
		except Exception as e:
			card = api.newCard(name=tasks[1][index], IdList=idList[0]["id"], date_start=now, date_last=now+datetime.timedelta(days=30) if tasks[2][index] is None else deadline(now, task[2][index]))
			answer = f"Задача №{index+1} для {name_} добавленна некорректно"

	return answer
		# print(id_user)

	# print(id_user)
	# answer = ["Задача была сохранена!",card['shortUrl']]


	# print(answer)
