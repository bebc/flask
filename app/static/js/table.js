$(function () {    
	var oTable = new TableInit();
	oTable.Init();
	$('#tb_departments').bootstrapTable('hideColumn','id')

	var oButtonInit = new ButtonInit();
	oButtonInit.Init();

});


var TableInit = function () {
	var oTableInit = new Object();
    
	oTableInit.Init = function () {
		$('#tb_departments').bootstrapTable({
			url: '/api/info',         
			dataType: "json",
			method: 'get',                      
			toolbar: '#toolbar',                
			striped: true,                      
			cache: false,                       
			pagination: true,                   
			sortable: false,                     
			sortOrder: "asc",                  
			queryParams: oTableInit.queryParams,
			//dataField: "infolist", 服务端分页
			sidePagination: "client",           
			pageNumber:1,                       
			pageSize: 1,                       
			pageList: [1, 2, 3, 4,10,20],       
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
				checkbox: true
			}, {
				field: 'id',
				title: 'id',
			},{
				field: 'ip',
				title: 'ip地址'
			}, {
				field: 'sys',
				title: '系统'
			}, {
				field: 'application',
				title: '用途'
			}, {
				field: 'OPE',
				title: '操作'
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

$('#add').click(function () {
	var addparams = $('#addform').serialize();
	var ip = $('#addip').val();
	if (ip == '') {
        $("#adderror").html("* ip必须填写");
        return ;
    }

    $.ajax({
        type: 'POST',
        url: '/api/addinfo',
        data: addparams,
        success: function(msg){
			if (msg == "addsuccess"){
				$('#tb_departments').bootstrapTable('refresh');
				//window.location.reload();
				//window.location.herf = "/test1";
			}
			else if (msg == "addfail"){
				alert("ip exist");
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
		//a = JSON.stringify(delraw);
		//alert(a);
		//alert(typeof(a));
		return delraw;
	});
	//a = JSON.stringify(raw);
	//alert(raw[0].ip+raw[0].sys);
	$.ajax({
		type: 'POST',
		url: '/api/delinfo',
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

$('#btn_edit').click(function () {
	var updateraw = $.map($('#tb_departments').bootstrapTable('getSelections'),function(updateraw){
        return updateraw;
	});
	//alert(updateraw[0].id);
	$('#updateid').val(updateraw[0].id);
	$("#updateip").val(updateraw[0].ip);
	$("#updatesys").val(updateraw[0].sys);
	$("#updateapplication").val(updateraw[0].application);
});
	

$('#update').click(function () {
	
    var updateparams = $('#updateform').serialize();
    var ip = $('#updateip').val();
    if (ip == '') {
        $("#updateerror").html("* ip必须填写");
        return ;
    } 

    $.ajax({
        type: 'POST',
        url: '/api/updateinfo',
        data: updateparams,
        success: function(msg){
            if (msg == "updatesuccess"){
                $('#tb_departments').bootstrapTable('refresh');

			}
            else if (msg == "updatefail"){
                alert("updatefail");
            }
            $('#myupdateModal').modal('hide');
            $(function () { $('#myupdateModal').on('hidden.bs.modal',function() {
                $('input').val('');
                })
            });
        },
        error: function(){
            alert("false");
        }
    });
});

