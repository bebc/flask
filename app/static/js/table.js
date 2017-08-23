$(function () {
    
    var oTable = new TableInit();
    oTable.Init();

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
            pageList: [1, 2, 3, 4],       
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
                title: 'id'
            }, {
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

   /* 服务端分页传值 
    oTableInit.queryParams = function (params) {
        var temp = {   
            limit: params.limit,   
            offset: params.offset,  
            
        };
        return temp;
    }; */ 
    return oTableInit;
};


var ButtonInit = function () {
    var oInit = new Object();
    var postdata = {};

    oInit.Init = function () {
       
    };

    return oInit;
};
