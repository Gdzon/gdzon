
$(function () {
    $("ul.nav > li").click(
        function () {
            $(this).find("ul").slideToggle();
        }
    )
});

$(document).ready(function() {
    $(".nav-klass-active").find("ul").slideToggle();
});