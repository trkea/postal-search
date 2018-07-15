function checkValue() {
	searchName = document.getElementById("searchName");
	if(searchName == "" || searchName == null) {
		document.getElementByClassName("searchForm").innerHTML('<div class="alert alert-warning" role="alert"><strong>Warning!</strong>入力して下さい</div>')
	}
}