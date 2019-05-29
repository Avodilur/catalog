$(document).ready(function () {
    $('.menu a').each(function(){
        if(document.location.href == this.href) {
            $(this).parent().prev().addClass('open');
        }
    })
})