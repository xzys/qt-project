var categoryType;
function displayListings(result) {
	var listingsElement = $("#listings");
	listingsElement.empty();
	for (i=0;i<result.length;i++) {
		var fields = result[i].fields;
		var toAppend = '<div class="panel panel-default"><div class="panel-body">';
		if (categoryType == 'A') {
			toAppend = toAppend + '<h1>' + fields.title '</h1>';
			toAppend = toAppend + '<span class="centerAlign">$50</span>';
			toAppend = toAppend + '<br>' + fields.isbn;
			toAppend = toAppend + '<span class="centerAlign">North Campus</span>';
			toAppend = toAppend + '<br>' + fields.condition;
		} else if (categoryType == 'B') {
			toAppend = toAppend + fields.event;
			toAppend = toAppend + '<span class="centerAlign">$10</span>';
			var date = new Date(fields.date);
			toAppend = toAppend + '<br>' + date.toLocaleString("en-US");
			toAppend = toAppend + '<span class="centerAlign">North Campus</span>';
		}
		toAppend = toAppend + '<br></div></div></div>';
		listingsElement.append(toAppend);
	}
}

function search() {
	var query = $("#searchBox").val();
	$.get(
		'http://localhost:8000/api/search', 
		{ 
			category: categoryType,
			q: query
		},
	    function(result) {
	    	var description = result.other;
	 		var firstPart = description.substring(0,description.lastIndexOf(" "));   	
	 		var secondPart = description.substring(description.lastIndexOf(" ")+1);   	
	    	$("#resultDescription").show();
	    	console.log(firstPart);
	    	console.log(secondPart);
	    	console.log(firstPart + '<a href="#">'+secondPart+'</a>');
	    	$("#resultDescription").html(firstPart + ' <a href="/'+secondPart.toLowerCase()+'?q='+query+'">'+secondPart+'</a>');
	    	displayListings(result.listings);
		}
	);
}

function requestListings (category) {
	$.get(
		'http://localhost:8000/api/getjson', 
		{ category: category },
	    function(result) {
<<<<<<< Updated upstream
	    	var listingsResponse = result.listings;
			for (i=0;i<listingsResponse.length;i++) {
				var fields = listingsResponse[i].fields;
				var toAppend = '<div class="panel panel-default"><div class="panel-body">';
				if (category == 'A') {
					toAppend = toAppend + "<span class='h3' style='float:left'>" + fields.title + "</span>" + "<div class = float:right style='width:50%'>" + "<span class='h3' style='float:right'>" + fields.price + "</span>" + "</div>";
					// toAppend = toAppend + "<span class='h3' style='float:left'>" + fields.title + "</span>";
					// toAppend = toAppend + "<span style='float:right'>" + fields.price + "</span>";
					// toAppend = toAppend + "<span class='h3' style='float:right'>" + fields.price + "</span>";
					// toAppend = toAppend + '<span class="centerAlign">$50</span>';
					toAppend = toAppend + "<br>" + fields.isbn;
					toAppend = toAppend + "<br>" + '<span class="centerAlign">North Campus</span>';
					toAppend = toAppend + "<br>" + fields.condition;
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
=======
	    	displayListings(result.listings);
>>>>>>> Stashed changes
		}
	);
}

function requestSignOut(){
	window.location.href = "http://localhost:8000/logout";
}

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
	var pathName = window.location.href;

	var modalBody = $(".modal-body");
	var postMods;
	if (pathName.indexOf("textbooks") != -1) {
		categoryType = 'A';
		$("#postListingBtn").html($("#postListingBtn").html() + "Textbook");
		$("#myModalLabel").html($("#myModalLabel").html() + "Textbook");
		$("#textbooks").addClass("activeCategory");
		postMods = ["ISBN", "Book Title", "Author", "Condition"];
	} else if (pathName.indexOf("tickets") != -1) {
		categoryType = 'B';
		$("#postListingBtn").html($("#postListingBtn").html() + "Ticket");
		$("#myModalLabel").html($("#myModalLabel").html() + "Ticket");
		$("#tickets").addClass("activeCategory");
		postMods = ["Event", "Date"];
	}

	var question = pathName.indexOf("?");
	if (question != -1) {
		var query = pathName.substring(question+1);
		$("#searchBox").val(pathName.substring(pathName.indexOf("q=")+2));
		search();
	} else {
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
	
	$('#searchBox').focus();
	$('#searchBox').keyup(function () { 
		// if textbox == null, then hide resultDescription
		search();
	});

	$("#SignOut").click(function() {
		requestSignOut();
	});
});