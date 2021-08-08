let input = document.querySelector('.input__file');

let label = input.nextElementSibling,
labelVal = label.querySelector('.input__file-button-text').innerText;

input.addEventListener('change', function (e) {

	console.log(this.files[0])
	let countFiles = this.files[0].name;
	let blocks = document.querySelectorAll('.block-message.space') 
	blocks.forEach( (event) => {
		event.remove()
	});

	if (this.files[0].type.split("/")[0] == "audio"){
		if (countFiles){ 
			label.querySelector('.input__file-button-text').innerText =countFiles; 
			document.querySelector('.icon-file').className = 'icon-file sendfile'; 
			// document.querySelector('.loader').className = 'loader start'; 

			var formData = new FormData();
			formData.append("file", this.files[0], countFiles);

			sendVoice(formData)
			// document.querySelector('.voiceform').submit()
		}
		else{ 
			label.querySelector('.input__file-button-text').innerText = labelVal; 
			document.querySelector('.icon-file').className = 'icon-file'
		}
	}
	else{ label.querySelector('.input__file-button-text').innerText = "Файл не подходит"; document.querySelector('.icon-file').className = 'icon-file'}
});
