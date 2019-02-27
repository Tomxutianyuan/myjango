$(function () {
    $('#not_login').click(function () {
        // console.log('=====>')
        window.open("/app/login", target = "_self")
    });

    $('#regis').click(function () {
        window.open("/app/register", target = "_self")
    })

})