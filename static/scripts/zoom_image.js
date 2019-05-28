$(document).ready(function() {
            $('.product-photo img').click(function() {
                var imgAddr = $(this).attr("src");
                $('#big_image img').attr({src: imgAddr});
                $('#big_image').fadeIn('slow');
            });
            $('#big_image').click(function() {
                $(this).fadeOut();
            });
        });