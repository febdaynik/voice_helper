from flask import Flask, render_template, request, jsonify
import voice, datetime, os, cfg_dev
import api_trello as api
import test_trello

app = Flask(__name__, static_folder="static_dir")
app.config['UPLOAD_FOLDER'] = 'files/'

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
		print(message)
		if not answer:
			text = voice.dot_in_text(message)
			answer = test_trello.main(text)

	return jsonify({"message":message, "fn":file_name, "answer_server":answer})



if __name__ == "__main__":
	app.run()