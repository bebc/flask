$(document).ready(function() {
	$(function() {
		$.ajax({
			type: "GET",
			url: "/api/info",
			dataType: "json",
			success: function(result) {
				addBox(result);
			}
		});
	});
	function addBox(result) {
		$.each(result,function(index,obj) {
			$("#box").append("<tr><td>"+obj.id+"</td><td>"+obj.ip+"</td><td>"+obj.sys+"</td><td>"+obj.application+"</td><td>"+"<button class='btn btn-xs btn-primary' type='button'>Mini button</button>&nbsp;<button class='btn btn-xs' type='button'>Mini button</button>"+"</td></tr>");
		});
	};
});
