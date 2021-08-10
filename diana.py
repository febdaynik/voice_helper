def split_word_task(word):
	words = [
		"выполняет задание", 
		"делает задание", 
		"задание"
	] 
	dedline = [
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
		if word.split(task_word).__len__() > 1:
			task = [i.strip() for i in word.split(task_word)]; break

	for dedline_word in dedline:
		if task[1].split(dedline_word).__len__()>1:
			return task[0],[i.strip() for i in task[1].split(dedline_word)]
	else:
		task[1] = [task[1],None]
		return task
