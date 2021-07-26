import requests, datetime, os

query = {
	"key": os.environ["APIkey"],
	"token": os.environ["APItoken"]
}


def getIdList(IdBoard):
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
