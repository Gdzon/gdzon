$(function () {
    $("ul.nav").accordion({
        heightStyle: "content",
        collapsible: true,
        animate: 230
    });
});

$(document).ready(function () {
    var index = $('ul.nav').find('ul');
    for (var j = 0; j < index.length; j++) {
        if (index[j].classList.contains('nav-klass-active')) {
            $('ul.nav').accordion('option', 'animate', 0);
            $('ul.nav').accordion('option', 'active', j);
        }
    }
    $('ul.nav').accordion('option', 'animate', 230);
});

$(window).scroll(function () {
    var top = $(document).scrollTop();
    if (top < 105) {
        $(".header").removeClass('fixed');
        $('.left-column-and-content').css('padding-top', '0')
    } else {
        $('.left-column-and-content').css('padding-top', '80px')
        $(".header").addClass('fixed');
    }
});

$(function () {
    $(".open-nav-button").click(function (){
        $(this).toggleClass('opened').toggleClass('closed').next().toggle();
            if($(this).hasClass('opened')) {
                $('.content').hide();
                $('.left-column').show().css("width", "100%");
                $('.logo').show();
            }
            else {
                $('.content').show();
                $('.left-column').hide();
                $('.logo').show();
            }
    });
});