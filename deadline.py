import datetime

calendar = {
	"января":"01",
	"февраля":"02",
	"марта":"03",
	"апреля":"04",
	"мая":"05",
	"июня":"06",
	"июля":"07",
	"августа":"08",
	"сентября":"09",
	"октября":"10",
	"ноября":"11",
	"декабря":"12"
}

	# elif "через" in text.lower():
	# 	date_ = text.split()
	# 	date_deadline = now + datetime.timedelta(days=int(date_[1]))

def deadline(now, text):
	try:
		print("TEXT:",text)
		if text.lower() == "завтра":
			date_deadline = now + datetime.timedelta(days=1)
		elif text.lower() == "после завтра":
			date_deadline = now + datetime.timedelta(days=2)
		else:
			date_ = text.split() 
			print("TEXT SPLIT:",date_)
			date_deadline = datetime.datetime.strptime(f"{date_[0]}.{calendar[date_[1]]}.{now.year}", '%d.%m.%Y')
			if (date_deadline-now).days < 0:
				date_deadline += datetime.timedelta(days=365)
	except Exception as e:
		date_deadline = now+datetime.timedelta(days=30)

	return date_deadline



