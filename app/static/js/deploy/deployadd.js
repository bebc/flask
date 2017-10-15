function appselect() {
	$.ajax({
        type: 'POST',
        url: '/api/appselect',
        dataType: 'json',
        success: function(msg){
            $.each(msg,function(){
                $('#web_project').append("<option>"+this+"</option>")
            });
        },
        error: function(){
            alert("false");
        }
    });
};
$(document).ready(function(){
	appselect();
});

$('#web_project').change(function(){
    $('#web_server option').remove()
    $("#result p").remove()
	$.ajax({
        type: 'GET',
        url: '/api/web_server_select?webproject='+$(this).val(),
        dataType: "json",
        success: function (msg) {
            $.each(msg,function(){
                $('#web_server').append("<option>"+this+"</option>");
                $('.selectpicker').selectpicker('refresh');
            })
        },
        error: function () {
            alert("false");
        }
    })
});

$('#submit').click(function () {
    var params = $('#deployadd').serialize();
    /*console.log($('#web_project').val());
    console.log($('#web_server').val());
    console.log($('#deploy_version').val());*/
    var web_projetc = $('#web_project').val();
    var web_server = $('#web_server').val();
    var deploy_version = $('#deploy_version').val();
    if (web_projetc == null) {
        $("#web_project_error").html("* 发布项目必须填写");
        return false;
    }
    else if (web_server == null) {
        $("#web_server_error").html("* 部署目标必须填写");
        return false;
    }
    else if (deploy_version == '') {
        $("#deploy_version_error").html("* 版本号必须填写");
        return false;
    }

    $.ajax({
        type: 'POST',
        url: '/deploy/deploy_app',
        data: params,
        success: function(result){
            $("#result").append("<p>"+result["msg"]+"</p>");
        },
        error: function(){
            alert("false");
        }
    });

    setTimeout("websocket()",30000)
})

//websocket
function websocket (){
    var namespace = '/msg'
    var socket = io.connect('http://192.168.186.128:5000'+namespace);
    function a(){socket.emit('my event', {data: 'I\'m connected!'})};
    a()
    socket.on('connect', function(msg) {
        if (msg != undefined) {
            console.log(msg);
            $('#result').append("<p>"+msg["log"]+"</p>");
        }
    })
}



