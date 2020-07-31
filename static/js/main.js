$(function () {
    $("ul.nav > li").click(
        function () {
            $(this).find("ul").slideToggle();
        }
    )
})

