$(function () {

    $("#mypay").click(function () {

        console.log("支付");
        var result = confirm('确定要支付此订单吗？')
        if (result) {

            var orderid = $(this).attr("orderid");

            $.getJSON("/app/payed/", {"orderid": orderid}, function (data) {
                console.log(data)
                if (data.status == 'ok') {
                    // window.open('',target='')
                    window.location.href = '/app/mine/'
                } else {
                    alert('支付失败！')
                }
            })
        }
    })

})