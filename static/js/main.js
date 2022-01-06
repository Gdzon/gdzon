$(function () {
    $("ul.nav").accordion({
        heightStyle: "content",
        collapsible: true,
        animate: 230
    });
});

function standby(a, b) {
    document.getElementsByClassName('bookCover')[a-b].src = "../static/img/covers/ifnotbook.svg";}


$(document).ready(function () {
    $('html, body').animate({
        scrollTop: 0
    }, 100);
    $('.ui-state-active').removeClass('ui-state-active');
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
    if (top < 14) {
        $(".header").removeClass('fixed');
        $('.left-column-and-content').css('padding-top', '0')
    } else {
        $('.left-column-and-content').css('padding-top', '80px')
        $(".header").addClass('fixed');
    }
});

$(function () {
    $(".nav-button").click(function (){
        $(this).toggleClass('nav-btn-opened').toggleClass('nav-btn-closed').next().toggle();
        $('.left-column').toggleClass('left-column-btn-opened').next().toggle();
        if($('.nav-button').hasClass('nav-btn-opened')){
            $('.content').hide();
        }
        else{
            $('.content').show();
        }
        $('.logo').show();
    });
});

$(window).resize(function () {
    var width = $(document).width();
    if (width > 930) {
        $('.content').show();
    }
});
