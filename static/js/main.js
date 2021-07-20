$( function() {
    $( "ul.nav" ).accordion({
        heightStyle: "content",
        collapsible: true,
    });
});

$(document).ready(function() {
    var index = $('ul.nav').find('ul');
    for(var j = 0; j < index.length; j++){
        if(index[j].classList.contains('nav-klass-active')){
            $('ul.nav').accordion('option', 'active', j);
        }
    }
});

$(window).scroll(function() {
                var top = $(document).scrollTop();
                if (top < 105) {
                    $(".header").removeClass('fixed');
                    $('.left-column-and-content').css('padding-top','0')
                }
                else {
                    $('.left-column-and-content').css('padding-top','80px')
                    $(".header").addClass('fixed');
                }
            });
