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

$(document).ready(function () {
    $('.submenu a').each(function(){
        if(document.location.href === this.href) {
            $(this).parent().parents('.submenu').addClass('open');
        }
    })
});

$(document).ready(function(){
    $('#search_products input[name="q"]').autocomplete({
        source: '/catalog/search/',
        minLength: 2,
        appendTo: "#search_products"
    });
});
