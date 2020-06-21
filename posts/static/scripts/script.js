
var $form = $('.replyform');
$form.hide();


$(document).ready(function () {
    $('.replyBtn').on('click',function () {
        $(this).next().show();
        //$formhtml.fadeIn();
        $(this).remove();
    });
});