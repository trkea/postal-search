window.onload = function() {
	x = Number.parseFloat(document.getElementById('x').value);
	y = Number.parseFloat(document.getElementById('y').value);
var map = L.map('map').setView([y,x], 14);

//OSMレイヤー追加
L.tileLayer(
	'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
	{
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a>',
		maxZoom: 18
	}
).addTo(map);
}