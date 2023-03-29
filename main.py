import folium
# Crea un objeto de mapa centrado en una ubicación específica
mi_mapa = folium.Map(location=[40.4637, -3.7492], zoom_start=10)
# Agrega un marcador en la ubicación del centro de Madrid
folium.Marker(location=[40.4168, -3.7038],
              popup='Centro de Madrid').add_to(mi_mapa)
# Agrega un marcador en la ubicación del centro de Madrid
folium.Marker(location=[40.4168, -3.7038],
              popup='Centro de Madrid').add_to(mi_mapa)
# Guarda el objeto de mapa como un archivo HTML
mi_mapa.save('mapa.html')
