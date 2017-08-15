$(document).ready(function() {
	$("#ajaxbutton").click(function() {
		var params = $("#loginform").serialize();
	        $.ajax({
			type : "POST",
	                url : "/login",
                        data : params,
                        success: function(msg){
                             if (msg == "login"){
				     window.location.href = "/login";
			     }
       	                     if (msg=="not active"){
				     alert("fail!");
			     }
			},
		});
	});
});

