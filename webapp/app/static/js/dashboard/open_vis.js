$('.getparent').on('click', function () {

    console.log('Magic in Progress');
    magic = $(this).parent();
    magic.children('.content_vis').toggleClass('magicopen');

});