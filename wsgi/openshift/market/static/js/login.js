function send_login_request() {
	console.log("LOGGING IN");
	var net_id   = $("#netid").val();
	var password = $("#password").val();
	var csrf_token = $("#authentication_csrf_token").val()
	$.post('/authrequest/login', { 
		               csrfmiddlewaretoken: csrf_token,
		               net_id:net_id, 
		               password:password,
		              }, function(result) {
		              		console.log(result)
		              		if (result.login_status == "true") {
		              			redirect_to_marketplace();
		              		} else {
		              			$("#message").empty()
		              			$("#message").append(result.login_message+"<br><br>");
		              		}
						 })
}

function stage_registration() {
	console.log("WAIT I'M AN IDIOT")
	$("#stage_registration_button").hide()
	$("#login_button").hide()
	$("#reentry_container").show()
	$("#register_button").show()
}

function redirect_to_marketplace() {
	window.location.replace("/");
}

function send_register_request() {
	console.log("REGISTERING");
	var net_id   = $("#netid").val();
	var password = $("#password").val();
	var csrf_token = $("#authentication_csrf_token").val()
	$.post('/authrequest/register', { 
		               csrfmiddlewaretoken: csrf_token,
		               net_id:net_id, 
		               password:password,
		              }, function(result) {
		              		console.log(result)
		              		if (result.registration_status == "true") {
		              			redirect_to_marketplace();
		              		} else {
		              			$("#message").empty()
		              			$("#message").append(result.registration_message+"<br><br>");
		              		}
						 })
}

$(document).ready(function() {
	
});