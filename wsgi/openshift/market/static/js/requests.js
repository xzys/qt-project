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
					toAppend = toAppend + fields.title;
					toAppend = toAppend + '<span class="centerAlign">$50</span>';
					toAppend = toAppend + '<br>' + fields.isbn;
					toAppend = toAppend + '<span class="centerAlign">North Campus</span>';
					toAppend = toAppend + '<br>' + fields.condition;
				} else if (category == 'B') {
					toAppend = toAppend + fields.event;
					toAppend = toAppend + '<span class="centerAlign">$10</span>';
					console.log(fields.date);
					var date = new Date(fields.date);
					toAppend = toAppend + '<br>' + date.toLocaleString("en-US");
					toAppend = toAppend + '<span class="centerAlign">North Campus</span>';
				}
				toAppend = toAppend + '<br></div></div></div>';
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