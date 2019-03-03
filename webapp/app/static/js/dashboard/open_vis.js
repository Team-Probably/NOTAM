$('.collapsible-header').on('click', function () {

    console.log('Magic in Progress');
    magic = $(this).parent();

    setTimeout(function () {
        console.log('Wait is over');
        //magic.children('.content_vis').toggleClass('magicopen');
        magic_map = magic.find('#vismap')[0];
        console.log(magic_map);

        lat = magic.find('.coordlat')[0].innerHTML;
        long = magic.find('.coordlong')[0].innerHTML;

        circle_lat = magic.find('.circle_lat')[0].innerHTML;
        circle_lng = magic.find('.circle_lng')[0].innerHTML;
        circle_rad = magic.find('.circle_rad')[0].innerHTML;
        zoom = magic.find('.zoom')[0].innerHTML;
        zoom = parseInt(zoom);
        console.log(zoom);
        poly_lat = magic.find('.polylat');
        poly_lng = magic.find('.polylng');
        avg_lat = 0;
        avg_lng = 0;
        poly = []
        for (var i = 0; i < poly_lat.length; i++) {
            poly_lat[i] = poly_lat[i].innerHTML;
            avg_lat += parseFloat(poly_lat[i]);
            poly_lng[i] = poly_lng[i].innerHTML;
            avg_lng += parseFloat(poly_lng[i]);
            poly.push([poly_lat[i], poly_lng[i]])
        }
        avg_lat = avg_lat / poly_lat.length;
        avg_lng = avg_lng / poly_lat.length;
        console.log(poly_lat);


        if (circle_rad > 0) {
            var mapCenter = [circle_lat, circle_lng];
            var map = L.map(magic_map).setView(mapCenter, zoom);

            L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                // attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets',
                accessToken: 'pk.eyJ1Ijoia2l0ZXJldHN1IiwiYSI6ImNqc216MTExNzA2NDE0OW80bWhyNmwyMmoifQ.v7pnFYhTlfA59e_sMBMSBA'
            }).addTo(map);

            L.circle(mapCenter, {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius: circle_rad
            }).addTo(map);

        } else if (poly_lat[0] > 0) {
            var mapCenter = [avg_lat, avg_lng];
            var map = L.map(magic_map).setView(mapCenter, zoom);

            L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                // attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets',
                accessToken: 'pk.eyJ1Ijoia2l0ZXJldHN1IiwiYSI6ImNqc216MTExNzA2NDE0OW80bWhyNmwyMmoifQ.v7pnFYhTlfA59e_sMBMSBA'
            }).addTo(map);

            L.polygon(poly, {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.5
            }).addTo(map);
        } else {
            var mapCenter = [lat, long];
            var map = L.map(magic_map).setView(mapCenter, zoom);
            
            L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                // attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets',
                accessToken: 'pk.eyJ1Ijoia2l0ZXJldHN1IiwiYSI6ImNqc216MTExNzA2NDE0OW80bWhyNmwyMmoifQ.v7pnFYhTlfA59e_sMBMSBA'
            }).addTo(map);

            L.marker(mapCenter).addTo(map);
        }

    }, 300);
    

    
}); 