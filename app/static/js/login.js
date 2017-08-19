$(document).ready(function() {
	$("#ajaxbutton").click(function() {
		var params = $("#loginform").serialize();
		var username = $("#username").val();
		$.ajax({
			type : "POST",
			url : "/login",
			data : params,
			success: function(msg) {
				if (msg == "john") {
					$.cookie('username',username);
					window.location.href = "/index";
				}
				if (msg == "not active") {
					alert("fail!");
				}
			},
		});
	});
});
