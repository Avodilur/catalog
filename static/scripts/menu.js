$(document).ready(function () {
    $('.submenu a').each(function(){
        if(document.location.href === this.href) {
            $(this).parent().parents('.submenu').addClass('open');
        }
    })
})