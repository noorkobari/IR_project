function fun(){
    var v1 = document.getElementById("minlatInput").value;
      var v2 = document.getElementById("maxlatInput").value;
      var v3 = document.getElementById("minlonInput").value;
      var v4 = document.getElementById("maxlonInput").value;
   

          var corner1 = L.latLng(v1,v2),//الطول
          corner2 = L.latLng(v3, v4),//العرض
          bounds = L.latLngBounds(corner1, corner2)
      
        var rect = L.rectangle(bounds, {
          color: 'red',
          weight: 1,
        
        })
          rect.addTo(map);  
          map.fitBounds(bounds);

      }  
