$('#ip_addr_form').click(function(){
    $('#ip_addr option').remove()
    $("#result p").remove()
	$.ajax({
        type: 'POST',
        url: '/api/ip_info',
        dataType: "json",
        success: function (msg) {
            $.each(msg,function(){
                $('#ip_addr').append("<option>"+this+"</option>");
                $('.selectpicker').selectpicker('refresh');
            })
        },
        error: function () {
            alert("false");
        }
    })
});

//提交ansible任务
$('#submit').click(function () {
    $("#result p").remove()
    var params = $('#ansible_hoc').serialize();

    $.ajax({
        type: 'POST',
        url: '/ansibleapi/run_command',
        data: params,
        success: function(result){
            $("#result").append("<p>"+result["msg"]+"</p>");
        },
        error: function(){
            alert("false");
        }
    });

})