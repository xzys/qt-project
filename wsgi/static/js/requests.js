$(document).ready(function(){
	var areas = ["North Campus", "West Campus", "Collegtown"];
	var filtersContainer = $('#filters');
	for (i=0; i<areas.length; i++) {
		filtersContainer.append('<input type="checkbox" value="'+ areas[i] + '"/> ' + areas[i] + '<br />');
	}

	var sorts = ["Item", "Price"];
	var sortContainer = $('#sorts');
	for (i=0; i<sorts.length; i++) {
		sortContainer.append('<button type="button" class="btn btn-default"> ' + sorts[i] + '</button>');
	}

	// var areas = ["Name v", "Price v"];
	// var checkboxContainer = $('#checkboxes');
	// for (i=0; i<areas.length; i++) {
	// 	checkboxContainer.append('<input type="checkbox" value="'+ areas[i] + '"/> ' + areas[i] + '<br />');
	// }
});