$('.getparent').on('click', function () {

    console.log('Magic in Progress');
    magic = $(this).parent();
    magic.children('.content_vis').toggleClass('magicopen');
    magic_map = magic.find('#vismap')[0];
    console.log(magic_map);
    lat = magic.find('.coordlat')[0].innerHTML;
    long = magic.find('.coordlong')[0].innerHTML;
    console.log(lat);
    var mapCenter = [lat, long];
    var map = L.map(magic_map).setView(mapCenter, 14);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        // attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1Ijoia2l0ZXJldHN1IiwiYSI6ImNqc216MTExNzA2NDE0OW80bWhyNmwyMmoifQ.v7pnFYhTlfA59e_sMBMSBA'
    }).addTo(map);
}); 