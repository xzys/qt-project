function requestListings (category) {
	var listings = $("#listings");
	$.get(
		'http://localhost:8000/api/getjson', 
		{ category: category },
	    function(result) {
	    	var listingsResponse = result.listings;
			for (i=0;i<listingsResponse.length;i++) {
				var fields = listingsResponse[i].fields;
				var toAppend = '<div class="panel panel-default"><div class="panel-body">';
				if (category == 'A') {
					toAppend = toAppend + fields.title + '<br>' + fields.isbn + '<br>' + fields.condition;
				} else if (category == 'B') {
					toAppend = toAppend + fields.event + '<br>' + fields.date;
				}
				toAppend + '</div></div></div>';
				listings.append(toAppend);
			}
		}
	);
}

function requestSignOut(){
	window.location.href = "http://localhost:8000/logout";
}

$(document).ready(function() {
	var pathname = window.location.pathname;
	if (pathname.indexOf("textbooks") != -1) {
		$("#textbooks").addClass("activeCategory");
		requestListings('A');
	} else if (pathname.indexOf("tickets") != -1) {
		$("#tickets").addClass("activeCategory");
		requestListings('B');
	}

	$("#SignOut").click(function() {
		requestSignOut();
	});
});