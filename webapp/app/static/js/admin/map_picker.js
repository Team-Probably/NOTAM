var mapCenter = [22, 87];
var map = L.map('map_picker').setView(mapCenter, 3);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    // attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoia2l0ZXJldHN1IiwiYSI6ImNqc216MTExNzA2NDE0OW80bWhyNmwyMmoifQ.v7pnFYhTlfA59e_sMBMSBA'
}).addTo(map); 

var marker = L.marker(mapCenter).addTo(map);
var updateMarker = function (lat, lng) {
    marker
        .setLatLng([lat, lng])
        .bindPopup("Your location :  " + marker.getLatLng().toString())
        .openPopup();
    return false;
};
map.on('click', function (e) {
    $('#latin').val(e.latlng.lat);
    $('#longin').val(e.latlng.lng);
    updateMarker(e.latlng.lat, e.latlng.lng);
});

var updateMarkerByInputs = function () {
    
    return map.flyTo([$('#latin').val(), $('#longin').val()], 12);
}
$('#latin').on('input', updateMarkerByInputs);
$('#longin').on('input', updateMarkerByInputs);