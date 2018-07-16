function jump() {
	city = document.getElementByTagName('a').value;
	window.location.href = 'http://127.0.0.1:8000/postal/town/?select=' + city;
}