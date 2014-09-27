$(document).ready(function(){
	$.get(
		'http://localhost:8000/api/getjson', 
		{ category: 'B' },
	    function(result) {
			console.log(result);
		}
	);
});