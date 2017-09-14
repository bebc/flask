var webproject = null;

$(function () {    
	var oTable = new TableInit();
	oTable.Init(webproject);
	$('#tb_departments').bootstrapTable('hideColumn','id')

	var oButtonInit = new ButtonInit();
	oButtonInit.Init();

});


$('#appquery').click(function() {
    var webproject = $('#appselect').val();
	var a = {
		url:'/api/appinfo?webproject='+webproject,
		silent:true,
	};
    $('#tb_departments').bootstrapTable('refresh',a);

});

var TableInit = function (webproject) {
	var oTableInit = new Object();
    
	oTableInit.Init = function (webproject) {
		console.log(webproject)
		var url='/api/appinfo?webproject='+webproject
		console.log(url)
		$('#tb_departments').bootstrapTable({
			url: url, 
			dataType: "json",
			method: 'get',                      
			toolbar: '#toolbar',                
			striped: true,                      
			cache: false,                       
			pagination: true,                   
			sortable: true,                     
			sortOrder: "asc",                  
			queryParams: oTableInit.queryParams,			
			sidePagination: "client",           
			pageNumber:1,                       
			pageSize: 3,                       
			pageList: [1, 3, 5,10,20],       
			search: true,                      
			strictSearch: true,
			showColumns: true,                 
			showRefresh: true,                 
			minimumCountColumns: 2,            
			clickToSelect: true,               
			height: 500,                       
			uniqueId: "ID",                    
			showToggle:true,                   
			cardView: false,                    
			detailView: false,                  
			columns: [{
				checkbox: true,
			}, {
				field: 'id',
				title: 'id',
			},{
				field: 'ip',
				title: 'ip地址',
			}, {
				field: 'webserver',
				title: '应用服务器',
			}, {
				field: 'webproject',
				title: '应用工程',
			}, {
				field: 'OPE',
				title: '操作',
			},]
		});
	};
	
	/*服务端分页传值		
	oTableInit.queryParams = function (params) {
		var temp = {   
			limit: params.limit,   
			offset: params.offset,  			
		};
		return temp;
	};*/
	return oTableInit;
};


var ButtonInit = function () {
	var oInit = new Object();
	var postdata = {};

	oInit.Init = function () {
	   
	};

	return oInit;
};

function appselect() {
	$.ajax({
        type: 'POST',
        url: '/api/appselect',
        dataType: 'json',
        success: function(msg){
            $.each(msg,function(){
                $('#appselect').append("<option>"+this+"</option>")
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


$('#btn_add').click(function () {
    var addraw = $.map($('#tb_departments').bootstrapTable('getSelections'),function(addraw){
        return addraw;
    });
    addip = addraw[0].ip;
    addappwebserver = addraw[0].webserver;
	$("#addip").html(addip);
	$("#addappwebserver").html(addappwebserver);
});

$('#appadd').click(function () {
   	var params = $('#addform').serialize();
	var addparams = params+"&addip="+addip+"&addappwebserver="+addappwebserver
	var addappproject = $('#addappproject').val();
	if (addappproject == '') {
       	$("#addappprojecterror").html("* 应用工程必须填写");
       	return ;
   	}

 	$.ajax({
       	type: 'POST',
       	url: '/api/appadd',
       	data: addparams,
       	success: function(msg){
           	if (msg == "appaddsuccess"){
               	$('#tb_departments').bootstrapTable('refresh');
           	}	
            else if (msg == "appaddfail"){
               	alert("appaddfail");
           	}
			else if (msg == "appexist"){
				alert("appexist")
			}
            $('#myaddModal').modal('hide');
            $(function () { $('#myaddModal').on('hidden.bs.modal',function() {
               	$('input').val('');
               	})
           	});
        },
        error: function(){
           	alert("false");
        }
    });
});

$('#btn_delete').click(function () {
    var delraw = $.map($('#tb_departments').bootstrapTable('getSelections'),function(delraw){
	return delraw;
    });
	$.ajax({
        type: 'POST',
        url: '/api/appdel',
        data: JSON.stringify(delraw),
        contentType: 'application/json',
        success: function(msg) {
            if (msg == "delsuccess"){
                $('#tb_departments').bootstrapTable('refresh');
            }
            else if (msg == "delfail"){
                alert("delfail")
            }
        },
        error: function(){
            alert("false");
        }
    });
});

