
function multiMarkerMap() {
  var locations = [];
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    const obj = JSON.parse(this.responseText);
    for (var i = 0; i < obj.length; i++){
      locations.push([obj[i][3], obj[i][2], obj[i][1], i+1]);
    }
    // console.log(locations);
  }
  
  xhttp.open("POST", "/api/get_stations_info", false);
  xhttp.setRequestHeader("kkey_y", "c9f53a7a0657ed8769098ad48074709cbd0bf0ad83e41e67164a9316605b86b0bdd81f0b16fd8b1a4a3dc7c0194f9bcb50cc29c16bfd73ef42c07e81b35026ef");
  xhttp.send("");

  var center = new google.maps.LatLng(51.9194, 19.1451);
  var map = new google.maps.Map(document.getElementById("multiMarkerMap"), {
    zoom: 5.5,
    center: center,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  var infowindow = new google.maps.InfoWindow();

  var marker, i;

  for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map
    });

    google.maps.event.addListener(
      marker,
      "click",
      (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        };
      })(marker, i)
    );
  }
}
function initMap() {
  multiMarkerMap();
}


// if (document.getElementById("google-map")) {
//   google.maps.event.addDomListener(window, "load", multiMarkerMap);
// }
