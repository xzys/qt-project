$(document).ready(function(){
	var url = "localhost:8000/api/getjson";
	var settings = {
		data: 'category=A',
	};
	// $.ajax(url, settings).done(function(result) {
	// 	var result = JSON.parse(result);
	// 	console.log(result);
	// });
	$.get(
		"localhost:8000/api/getjson", 
		{ category: 'A' },
	    function(result) {
			var result = JSON.parse(result);
			console.log(result);
		}
	);
});