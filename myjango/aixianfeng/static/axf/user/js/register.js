$(function () {

    var $username = $("#username_input");

    $username.blur(function () {
        var username = $username.val().trim()
        var $username_info = $('#username_info')
        if (username.length > 0) {
            $.getJSON('/app/checkname', {'username': username}, function (data) {


                if (data.status == 'fail') {
                    $username_info.text(data.msg).css('color', 'red')
                } else {
                    $username_info.text(data.msg).css('color', 'green')
                }
            })
        } else {
            $username_info.text('用户名不能为空').css('color', 'red')
        }
    })


})


function check() {
    var $username = $("#username_input");

    var username = $username.val().trim();

    if (!username) {
        return false
    }

    var info_color = $("#username_info").css('color');

    console.log(info_color);

    if (info_color == 'rgb(255, 0, 0)') {
        return false
    }

    var $password_input = $("#password_input");

    var password = $password_input.val().trim();

    $password_input.val(md5(password));

    return true
}
