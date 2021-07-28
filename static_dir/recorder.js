var recordButton, stopButton, recorder;

window.onload = function () {
	recordButton = document.getElementById('record');
	stopButton = document.getElementById('stop');

	navigator.mediaDevices.getUserMedia({audio: true})
	.then(function (stream) {
		recordButton.addEventListener('click', startRecording);
		stopButton.addEventListener('click', stopRecording);
		recorder = new MediaRecorder(stream);

		recorder.addEventListener('dataavailable', onRecordingReady);
	});
};

function startRecording() {
	let blocks = document.querySelectorAll('.block-message.space') 
	blocks.forEach( (event) => {
		event.remove()
	});
	recordButton.classList.toggle("disabled")
	stopButton.classList.toggle("disabled")
	recorder.start();
}

function stopRecording() {
	recordButton.classList.toggle("disabled")
	stopButton.classList.toggle("disabled")
	recorder.stop();
}

function onRecordingReady(e) {
	// var audio = document.getElementById('audio');
	// audio.src = URL.createObjectURL(e.data);
	const audioBlob = new Blob([e.data], {type: 'audio/ogg'});

	let fd = new FormData();
    fd.append('file', audioBlob);
	sendVoice(fd);

	// audio.play();
}

function sendVoice(form) {
	xhr = new XMLHttpRequest()
	xhr.open('POST', document.location.href+"recorder");
	xhr.send(form);
	document.querySelector('.loader').classList.toggle('start');
	xhr.onreadystatechange = function() {
		if (xhr.readyState != 4) return;
		if (xhr.status == 200){
			document.querySelector('.loader').classList.toggle('start');
			answ = JSON.parse(xhr.response)
			console.log(answ)
			let contentblock = document.querySelector('.content-block');
			if (answ.message){
				contentblock.insertAdjacentHTML("beforeEnd", `<div class="block-message space">
						<span class="label-audio">Текст из файла:</span><p class="text-audio">${ answ.message }</p>
						<span class="label-audio">Аудио</span><div class="block-audio">
							<audio controls>
								<source src="${ answ.fn }" type="audio/wav">
							</audio>
						</div>
					</div>`)
			}
			if (answ.answer_server && typeof(answ.answer_server) == "object"){
				contentblock.insertAdjacentHTML("beforeEnd", `<div class="block-message space">
						<div class="label-audio block-link-task">
							<p>${ answ.answer_server[0] }</p>
							<p class="error">${ answ.answer_server[2] }</p>
							<a href="${ answ.answer_server[1] }">Ссылка на задачу</a>
						</div>
					</div>`)
			}
			else if (answ.answer_server && typeof(answ.answer_server) == "string"){
				contentblock.insertAdjacentHTML("beforeEnd", `<div class="block-message space">
						<div class="label-audio block-link-task">
							<p>${ answ.answer_server }</p>
						</div>
					</div>`)
			}
		}
	}


}

