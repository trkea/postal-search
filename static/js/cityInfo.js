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

function getParam() {
        var url   = location.href;
        parameters    = url.split("?");
        params   = parameters[1].split("&");
        var paramsArray = [];
        for ( i = 0; i < params.length; i++ ) {
            neet = params[i].split("=");
            paramsArray.push(neet[0]);
            paramsArray[neet[0]] = neet[1];
        }
        var categoryKey = paramsArray["key"];
        return categoryKey;
	}

$(function() {
$('#favorite').click(function() {
  $.get('/postal/favorite',
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