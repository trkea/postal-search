function checkValue() {
	searchName = document.getElementById("searchName").value;
	if(searchName === "" || searchName === null) {
		nullAlert()
		return false;
	}
	return true
}

function nullAlert() {
	$('.alert').html('<div class="alert alert-warning" role="alert">入力して下さい</div>').fadeOut(2000)
	 setTimeout(function(){
        $('.alert').html('');
    },2000);
}