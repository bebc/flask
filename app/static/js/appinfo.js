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
	var oTable = new TableInit();
    oTable.Init(webproject);
   // $('#tb_departments').bootstrapTable('refresh');

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


