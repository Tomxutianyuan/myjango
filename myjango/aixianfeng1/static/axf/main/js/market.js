$(function () {

    $("#all_types").click(function () {

        console.log("全部类型");

        var $all_types_container = $("#all_types_container");

        $all_types_container.slideDown();
        // 将span标签的箭头改变成向上的

        var $all_type = $(this);

        var $span = $all_type.find('span').find('span')

        $span.removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        var $sort_rule_container = $('#sort_rule_container')
        $sort_rule_container.slideUp()

        var $sort_rule = $('#sort_rule')

        var $span = $sort_rule.find('span').find('span')

        $span.removeClass("glyphicon-chevron-up").addClass('glyphicon-chevron-down')

    })

    $("#all_types_container").click(function () {
        var $all_types_container = $(this)
        $all_types_container.slideUp()
        var $all_types = $('#all_types')
        var $span = $all_types.find('span').find('span')
        $span.removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
    })


    $("#sort_rule").click(function () {

        console.log("排序规则");

        var $sort_rule_container = $("#sort_rule_container");

        $sort_rule_container.slideDown();

        var $sort_rule = $(this);

        var $span = $sort_rule.find("span").find("span");

        $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");

        var $all_type_container = $("#all_types_container");

        $all_type_container.hide();

        var $all_type = $("#all_types");

        var $span_all_type = $all_type.find("span").find("span");

        $span_all_type.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");


    })

    $("#sort_rule_container").click(function () {

        var $sort_rule_container = $(this);

        $sort_rule_container.slideUp();

        var $sort_rule = $("#sort_rule");

        var $span = $sort_rule.find("span").find("span");

        $span.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })


    $(".subShopping").click(function () {
        console.log('sub');
    })

    $(".addShopping").click(function () {

        console.log('add');
        var $add = $(this);
        var id1 = $add.attr('gid')
        // var id2= $add.prop('gid')  <input type='checkbox' checked/>   <select><option selected> milk</option></select>
        $.getJSON('/app/addCart', {'gid': id1}, function (data) {
            console.log(data)
            if (data.status == 'fail') {
                // window.open('/app/login/', target = '_self')
                window.location.href='/app/login/'
            } else if (data.status == 'ok') {
                $add.prev('span').text(data.goods_num)
            }
        })
    })

})