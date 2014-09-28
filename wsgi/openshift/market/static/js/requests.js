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
					toAppend = toAppend + "<div class = float:left style='width:50%'>" + "<span class='h3' style='float:left'>" + fields.title + "</span>" + "</div>" + "<div class = float:right style='width:50%'>" + "<span class='h3' style='float:right'>" + fields.price + "</span>" + "</div>";
					// toAppend = toAppend + "<span class='h3' style='float:left'>" + fields.title + "</span>";
					// toAppend = toAppend + "<span style='float:right'>" + fields.price + "</span>";
					// toAppend = toAppend + "<span class='h3' style='float:right'>" + fields.price + "</span>";
					// toAppend = toAppend + '<span class="centerAlign">$50</span>';
					toAppend = "<br>" + toAppend + fields.isbn;
					toAppend = "<br>" + toAppend + '<span class="centerAlign">North Campus</span>';
					toAppend = "<br>" + toAppend + fields.condition;
				} else if (category == 'B') {
					toAppend = toAppend + fields.event;
					toAppend = toAppend + '<span class="centerAlign">$10</span>';
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

var categoryType;
function submitPost() {
	var listings = $(".modal-body");
	var location = listings.find('[name="Location"]')[0].value;
	var price = parseFloat(listings.find('[name="Price"]').val());
	var isbn;
	var bookTitle;
	var author;
	var condition;
	var eventName;
	var eventDate;
	if (categoryType == 'A') {
		isbn = listings.find('[name="ISBN"]').val();
		bookTitle = listings.find('[name="Book Title"]').val();
		author = listings.find('[name="Author"]').val();
		condition = listings.find('[name="Condition"]')[0].value;
		event = '';
		eventDate = '';
	} else if (categoryType == 'B') {
		eventName = listings.find('[name="Event"]').val();
		eventDate = listings.find('[name="Date"]').val();
	}
	$.get(
		'http://localhost:8000/api/postlisting', 
		{ 
			category: categoryType,
			location: location,
			price: price,
			isbn: isbn,
			author: author,
			title: bookTitle,
			condition: condition,
			event: eventName,
			event_date: eventDate,
	 	},
	    function(result) {
    		console.log(result);
		}
	);
}

$(document).ready(function() {
	var pathname = window.location.pathname;
	var modalBody = $(".modal-body");
	var postMods;
	if (pathname.indexOf("textbooks") != -1) {
		categoryType = 'A';
		$("#postListingBtn").html($("#postListingBtn").html() + "Textbook");
		$("#myModalLabel").html($("#myModalLabel").html() + "Textbook");
		$("#textbooks").addClass("activeCategory");
		postMods = ["ISBN", "Book Title", "Author", "Condition"];
		requestListings(categoryType);
	} else if (pathname.indexOf("tickets") != -1) {
		categoryType = 'B';
		$("#postListingBtn").html($("#postListingBtn").html() + "Ticket");
		$("#myModalLabel").html($("#myModalLabel").html() + "Ticket");
		$("#tickets").addClass("activeCategory");
		postMods = ["Event", "Date"];
		requestListings(categoryType);
	}
	for (i=0;i<postMods.length;i++) {
		if (postMods[i] == "Condition") {
			modalBody.append('Condition: <select name="Condition"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5 (Best Condition)</option></select><br><br>');
		} else if (postMods[i] == "Date") {
			modalBody.append(postMods[i]+': <input type="date" name="'+postMods[i]+'"><br><br>');
		} else {
			modalBody.append(postMods[i]+': <input type="text" name="'+postMods[i]+'"><br><br>');
		}
	}

	modalBody.append('Price: <input type="text" name="Price" placeholder="$"><br><br>Your Location: <select name="Location"><option value="0">North Campus</option><option value="1">West Campus</option><option value="2">Collegetown</option></select>');
	
	$("#SignOut").click(function() {
		requestSignOut();
	});
});