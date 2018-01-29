import folium
import psycopg2 as pg
import datetime as dt
import pandas

data=pandas.read_csv('http://pythonhow.com/data/Volcanoes_USA.txt', sep=',')
volcanes = [list(data["LAT"]),list(data["LON"]),list(data["ELEV"])]

map = folium.Map(location=[8,-80],zoom_start=8)

#Funcion para que retorna string color dependiendo de la elevacion
def marker_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


conn = pg.connect("dbname=gisdata host=amts-svr4 user=ricardo")
cur = conn.cursor()
cur.execute("SELECT position_id,longitude,latitude, gnss_ts, imonumber from ais.ais_data limit 20")

#Se definen los grupos de las diferentes capas
fg_test = folium.FeatureGroup(name="Test Positions")
fg_ais = folium.FeatureGroup(name="AIS Position")
fg_polygons = folium.FeatureGroup(name="Polygons")
fg_volcanoes = folium.FeatureGroup(name="Volcanoes")




fg_test.add_child(folium.Marker(location=[8.50,-79.5],popup="Posicion de Prueba", icon=folium.Icon(color="lightgreen")))
fg_test.add_child(folium.Marker(location=[8.50,-77.5],popup="Otra posicion de Prueba", icon=folium.Icon(color="pink")))

#Carga los datos de la variable volcanes
for x, y, z  in zip(volcanes[0],volcanes[1], volcanes[2]):
    #fg.add_child(folium.Marker(location=[x,y], popup="Volcan # "+str(int(volcanes[0].index(x))+1) + " Elevación: "+str(z), icon=folium.Icon(color=marker_color(z))))
    fg_volcanoes.add_child(folium.CircleMarker(location=[x,y], popup="Volcan # "+str(int(volcanes[0].index(x))+1) + " Elevación: "+str(z), radius= 6, fill=1, color="grey", fill_color=marker_color(z), fill_opacity=0.8))


#Carga los puntos en la Base de datos en SVR4
for r in cur.fetchall():
    fg_ais.add_child(folium.Marker(location=[float(r[2]),float(r[1])],popup="IMO#"+str(r[4])+"\n"+r[3].strftime("%Y-%m %H:%M"), icon=folium.Icon(color="green")))


fg_polygons.add_child(folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig").read(),
style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"]<10000000
else "orange" if 10000000<=x["properties"]["POP2005"]<20000000 else "red" }))


map.add_child(fg_test)
map.add_child(fg_ais)
map.add_child(fg_polygons)
map.add_child(fg_volcanoes)
map.add_child(folium.LayerControl())
map.save("Panama1.html")
