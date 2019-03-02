var map = L.map('marker_map').setView([19.0896, 72.8656], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    // attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoia2l0ZXJldHN1IiwiYSI6ImNqc216MTExNzA2NDE0OW80bWhyNmwyMmoifQ.v7pnFYhTlfA59e_sMBMSBA'
}).addTo(map); 

var editableLayers = new L.FeatureGroup();
map.addLayer(editableLayers);


var options = {
    position: 'topleft',
    draw: {
        polyline: false,
        polygon: {
            allowIntersection: false, // Restricts shapes to simple polygons
            drawError: {
                color: '#e1e100', // Color the shape will turn when intersects
                message: '<strong>Oh snap!<strong> you can\'t draw that!' // Message that will show when intersect
            },
            shapeOptions: {
                color: '#d31f1f'
            }
        },
        circle:  {
            shapeOptions: {
                color: '#d31f1f'
            }
		}, // Turns off this drawing tool
        rectangle: {
                shapeOptions: {
                    color: '#d31f1f'
                }
            },
        marker: false,
        circlemarker: false 
    },
    edit: {
        featureGroup: editableLayers, //REQUIRED!!
        remove: true
    }
};

var drawControl = new L.Control.Draw(options);
map.addControl(drawControl);


radius = null
center = null
poly = null

map.on('draw:created', function (e) {

    var type = e.layerType,
        layer = e.layer;

    if (type === 'circle') {
        
        radius = layer.getRadius();
        center = layer.getLatLng();
        poly = null;
        
    } else {
        
        poly = layer.getLatLngs();
        radius = null;
        center = null;
        
    } 

    console.log(radius, center, rect);
    editableLayers.addLayer(layer);
});