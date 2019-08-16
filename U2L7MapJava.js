var map;
var ourLoc;
var view;

function init(){
  ourLoc = ol.proj.fromLonLat([-7.77832031, 53.2734]);
  view = new ol.View({
    center: ourLoc,
    zoom: 6  //can change this as you wish
  });
  map = new ol.Map({
    target:'map', //set in html as our <div> name
    layers:[
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view:view
  });
}

function panHome(){
  view.animate({
    center:ourLoc,
    duration:2000 // 2 seconds
  });
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;
  var lon= 0.0;
  var lat= 0.0;
  var query = "https://restcountries.eu/rest/v2/name/"+countryName;
  query = query.replace(/ /g, "%20");
  alert(query);
  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);
  countryRequest.send();
  //alert("Ready State "+countryRequest.readyState);
  //alert("Status "+ countryRequest.status);
  //alert("Response "+ countryRequest.responseText);
  if(countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText ===""){
    window.console.error("Request had an error");
    return;
  }
  var countryInformation = JSON.parse(countryRequest.responseText);
  var lat = countryInformation[0].latlng[0];
  var lon = countryInformation[0].latlng[1];
  var location= ol.proj.fromLonLat([lon,lat]);
  window.console.log(countryName + ": lon"+" & lat "+ lat)
  view.animate({
    center: location,
    duration: 2000
  });
}
window.onload = init;
