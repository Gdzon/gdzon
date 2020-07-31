$(function () {
    $("ul.nav > li").click(
        function () {
            $(this).find("ul").show("di");
            $(this).find("ul").css("display", "table-row-group")
        }
    )
})