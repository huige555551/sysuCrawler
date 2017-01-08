$(document).ready(function () {
    $.ajax({
        type: "GET",//提交方式
        url: "/api/scoreDetail",//路径
        success: function (result) {//返回数据根据结果进行相应的处理
                console.log(result)
                $("#content").html(result);
        }
    });
});