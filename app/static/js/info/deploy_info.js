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
			url: '/api/deploy_info',
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
			pageSize: 10,
			pageList: [1, 10, 20, 50],
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
				field: 'name',
				title: '用户',
			}, {
				field: 'web_project',
				title: '项目',
			}, {
				field: 'version',
				title: '版本号',
			}, {
				field: 'result',
				title: '执行结果',
			},{
				field: 'create_date',
				title: '创建时间',
			},{
				field: 'execute_date',
				title: '执行时间',
			}]
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