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


$(function() {
var prefecture = $('#prefecture').val();
var city = $('#city').val();
var town = $('#town').val();
var x = $('#x').val();
var y = $('#y').val();
var url = ('/postal?prefecture=' + prefecture + '&city=' + city + '&town=' + town + '&x=' + x + '&y=' + y);
$('#favorite').click(function() {
    $.get(url,
      {
        datatype:'html',
        data:{
        'prefecture':$('#prefecture').val(),
        'city':$('#city').val(),
        'town':$('#town').val(),
        'x':$('#x').val(),
        'y':$('#y').val(),
        },
        success:function() {
        　　alert(url);
            if($('#favorite').css('color') == 'rgb(255, 255, 0)') {
                $('#favorite').css('color','black')
            }else{
                $('#favorite').css('color','yellow')

        }
           },
      }
    );
});
});