
  (function ($) {
  
  "use strict";

    // NAVBAR
    $('.navbar-nav .nav-link').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    // REVIEWS CAROUSEL
    $('.reviews-carousel').owlCarousel({
        center: true,
        loop: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplaySpeed: 300,
        smartSpeed: 500,
        responsive:{
          0:{
            items:1,
          },
          768:{
            items:2,
            margin: 100,
          },
          1280:{
            items:2,
            margin: 100,
          }
        }
    });

    // Banner Carousel
    var myCarousel = document.querySelector('#myCarousel')
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 1500,
    })

    // REVIEWS NAVIGATION
    function ReviewsNavResize(){
      $(".navbar").scrollspy({ offset: -94 });

      var ReviewsOwlItem = $('.reviews-carousel .owl-item').width();

      $('.reviews-carousel .owl-nav').css({'width' : (ReviewsOwlItem) + 'px'});
    }

    $(window).on("resize", ReviewsNavResize);
    $(document).on("ready", ReviewsNavResize);

    // HREF LINKS
    $('a[href*="#"]').click(function (event) {
      if (
        location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          event.preventDefault();
          $('html, body').animate({
            scrollTop: target.offset().top - 74
          }, 1000);
        }
      }
    });
    
// $("#home/booking").on("submit", (e) => {
//   e.preventDefault();
//   const data = {
//     'name': $('input[name=name]').val(),
//     'email': $('input[name=email]').val(),
//     'phone': $('input[name=phone]').val(),
//     'date': $('input[name=date]').val(),
//     'content': $('textarea[name=content]').val(),
//     'csrfmiddlewaretoken': '{{ csrf_token }}'
//   };
//   $.post("http://127.0.0.1:8000/messages/receive_message/", data, () => {
//     console.log("all is okay");
//   });

//   e.target.reset();
//   });

$("#home/booking").on("submit", (e) => {
  e.preventDefault(); // Prevent the default form submission

  const data = {
    'name': $('input[name=name]').val(),
    'email': $('input[name=email]').val(),
    'phone': $('input[name=phone]').val(),
    'date': $('input[name=date]').val(),
    'content': $('textarea[name=content]').val(),
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() // Correct token retrieval
  };

  $.post("http://127.0.0.1:8000/messages/receive_message/", data)
    .done(() => {
      console.log("All is okay");
      alert("Appointment booked successfully!");
      e.target.reset(); // Reset the form
    })
    .fail((xhr, status, error) => {
      console.error("Error:", error);
      alert("Something went wrong. Please try again.");
    });
});

  })(window.jQuery);
