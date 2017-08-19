$(function(){
	var username = $.cookie('username');//获取存储的cookie
	$('#aa').html(username);//打印到页面上
})
