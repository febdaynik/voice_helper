import requests, datetime

# Артур ключи
# query = {
# 	"key":"c10a9b515c27095e719526ce58ea50b8",
# 	"token":"978e94d25b3e97518268c76f63d0151a9e948c39f0c4be1056dfaf3e3c6bdc34"
# }

# Мои ключи
query = {
	"key":"96c960faf9c0c2a49d4dd761fb62c590",
	"token":"17f8826c941fc48c54a837da43dc5555b8badb75b8267e2271edca7d5dfb4de5"
}


def getIdList(IdBoard: str = "60c78ce8498d4f195c7c51d2"):
	return requests.get(f"https://trello.com/1/boards/{IdBoard}/lists", params=query).json()

def newCard(name, IdList, date_start = None, date_last = None, description = None, members = None):
	return requests.post("https://trello.com/1/cards", params=query, data={"name":name, "desc":description,"idList":IdList, "start":date_start, "due":date_last, "idMembers":members}).json()

def getIdCard(IdList):
	return requests.get(f"https://trello.com/1/lists/{IdList}/cards", params=query).json()

def getMembers(IdBoard):
	return requests.get(f"https://trello.com/1/boards/{IdBoard}/members", params=query).json()

def addMembers(IdCard, value):
	return requests.post(f"https://trello.com/1/cards/{IdCard}/idMembers", params=query, data={ "value": value }).json()

def updateCard(IdCard, date_start = None, date_last = None, description = None, members = None):
	return requests.put(f"https://trello.com/1/cards/{IdCard}", params=query, data={"due":date_last, "start":date_start, "idMembers":members, "desc":description}).json()

if __name__ == '__main__':
	now = datetime.datetime.now()
	members_username = {
		"Иванов": "feb62",
		"Эпитов": 0,
		"Малютин": 0,
	}

	idList = getIdList(IdBoard = "60d0646f90d48645032c4820")
	members = getMembers(IdBoard = "60d0646f90d48645032c4820")
	id_user = [i["id"] for i in members if i["username"] == members_username["Иванов"]]
	card = newCard(name="Ещё одна карточка, хаха", IdList=idList[0]["id"], date_start=now, date_last=now+datetime.timedelta(days=5), members=[ id_user ])
	print(card["shortUrl"])
	# idCard = getIdCard(IdList = idList[0]["id"])
	# ans_member = addMembers(IdCard = idCard[0]["id"], value = members[0]["id"])
	# a = updateCard(IdCard = idCard[0]["id"], description="Какая-то задача на день")
	