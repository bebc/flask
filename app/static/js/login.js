$(document).ready(function() {
	$("#ajaxbutton").click(function() {
		var params = $("#loginform").serialize();
		var username = $("#username").val();
		$.ajax({
			type : "POST",
			url : "/user/login",
			data : params,
			success: function(msg) {
				if (msg == "loginsuccess") {
					$.cookie('username',username);
					window.location.href = "/index";
				}
				else if (msg == "not active") {
					alert("fail!");
				}
			},
		});
	});
});
