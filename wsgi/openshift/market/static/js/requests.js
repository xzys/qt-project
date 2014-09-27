$(document).ready(function(){
	$.get(
		'http://localhost:8000/api/getjson', 
		{ category: 'A' },
	    function(result) {
			console.log(result);
		}
	);
});