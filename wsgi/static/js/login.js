function send_login_request() {
	console.log("LOGGING IN");
	var net_id   = $("#netid").val();
	var password = $("#password").val();
	var csrf_token = $("#authentication_csrf_token").val()
	console.log("passing login request");
	$.post('/authrequest/login/', { 
		               csrfmiddlewaretoken: csrf_token,
		               net_id:net_id, 
		               password:password,
		              })
}

function send_register_request() {
	console.log("REGISTERING");
}

$(document).ready(function() {
	
});