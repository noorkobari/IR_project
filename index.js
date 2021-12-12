function fun(){
//var v1 = document.getElementById('minlatInput')
//var v2 = document.getElementById('maxlatInput')

var corner1 = L.latLng(40.712,100.227),//الطول
corner2 = L.latLng(12.774, 11.125),//العرض
bounds = L.latLngBounds(corner1, corner2)

    var rect = L.rectangle(bounds, {
    color: 'blue',
    weight: 1,
  
  
  }).addTo(map);

  map.fitBounds(bounds)

}