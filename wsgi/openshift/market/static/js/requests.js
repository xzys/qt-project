$(document).ready(function(){
	var listings = $("#listings");
	$.get(
		'http://localhost:8000/api/getjson', 
		{ category: 'A' },
	    function(result) {
	    	var listingsResponse = result.listings;
			for (i=0;i<listingsResponse.length;i++) {
				console.log(i);
				var fields = listingsResponse[i].fields;
				listings.append('<div class="panel panel-default"><div class="panel-body">'+
					fields.title + '<br>' + fields.isbn + '<br>' + fields.condition + 
					'</div></div></div>');
			}
		}
	);
});