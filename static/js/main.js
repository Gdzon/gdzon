$(document).ready(function(){
    var w=$(".content").outerHeight();
    $("#left-column-back").css({"height":w});
});


$(function () {
    $("ul.nav > li").click(
        function () {
            $(this).find("ul").slideToggle();
            $(this).find("ul").css("display","table-row-group");
        }
    )
})

