


$(function () {
    $("ul.nav > li").click(
        function () {
            $(this).find("ul").slideToggle();
            $(this).find("ul").css("display","table-row-group");
        }
    )
})

