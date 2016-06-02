$(document).ready(function(){

  // $('#menu-icons-wrapper')
  //   .velocity("fadeIn", { delay: 100, duration: 600 });

  $("figure")
    .velocity("transition.fadeIn", { delay: 500, stagger: 150, easing: "easeInQuint"} );

  $('#logo').click(function(){
    $('#mainContent').load('ajax.html');
  });

});


