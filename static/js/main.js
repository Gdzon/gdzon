
$( function() {
    $( "ul.nav" ).accordion({
      heightStyle: "content",
      collapsible: true
    });
  } );

$(document).ready(function() {
    $(".nav-klass-active").find("ul").slideToggle();
});