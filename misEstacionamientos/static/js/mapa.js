var mostrarMapa = false;

function cargarMapa() {
    var mapDiv = document.getElementById('mapa');
    mostrarMapa = !mostrarMapa;
    mapDiv.hidden = !mostrarMapa;
    if (!mostrarMapa) {
        document.getElementById('btnMapa').innerHTML = "Ver mapa";
        return;
    }
    document.getElementById('btnMapa').innerHTML = "Ocultar mapa";
    var latitud = Number.parseFloat(document.getElementById('latitud').innerHTML.replace(',', '.'));
    var longitud = Number.parseFloat(document.getElementById('longitud').innerHTML.replace(',', '.'));
var localizacion = new google.maps.LatLng(latitud,longitud);
var options = {
center: localizacion,
zoom: 15,
mapTypeId: google.maps.MapTypeId.ROADMAP
};
    var mapa = new google.maps.Map(mapDiv, options);
}
