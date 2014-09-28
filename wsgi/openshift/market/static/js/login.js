function resizeWindow() {
	var aspectRatio = 1.9;
	var windowWidth = $(window).width(); //1721
	var windowHeight = $(window).height(); // 449
	console.log("windowWidth: " + windowWidth);
	console.log("windowHeight: " + windowHeight);

	if (windowWidth / windowHeight < aspectRatio) {
		bodyWidth = windowHeight * aspectRatio;
		bodyHeight = windowHeight;
	} else {
		bodyHeight = windowWidth / aspectRatio; // 961
		bodyWidth = windowWidth; //1721
	}

	// if (windowHeight < 400) {
	// 	bodyHeight = 600;
	// 	bodyWidth = 1074;
	// }
	// console.log(bodyWidth);
	// console.log(bodyHeight);

	var container = $("#wrapper");
	container.css("width", bodyWidth + "px");
	container.css("height", bodyHeight + "px");
	console.log("NEW - Width: " + container.width() + " Height: " + container.height());
}

$(document).ready(function() {
	resizeWindow();
	$(window).resize(function() {
		console.log("resizing");
		resizeWindow();
	})
});