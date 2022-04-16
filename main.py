from flask import Flask, render_template
import openrouteservice
from openrouteservice.directions import directions
from openrouteservice import convert

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mayaO'

@app.route('/')
def hello():
    coords = ((8.54234,48.23424),(8.34423,48.26424))
    client = openrouteservice.Client(key='5b3ce3597851110001cf624867c31029cd564d6d99171dbb0990af67') # Specify your personal API key
    routes  = client.directions(coords,alternative_routes={"share_factor":0.6,"target_count":3,"weight_factor":1.4})
    
    geometry1 = routes['routes'][0]['geometry']
    decoded1 = convert.decode_polyline(geometry1)
    
    geometry2 = routes['routes'][1]['geometry']
    decoded2 = convert.decode_polyline(geometry2)

    geometry3 = routes['routes'][2]['geometry']
    decoded3 = convert.decode_polyline(geometry3)

    return render_template("main.html",route1=decoded1['coordinates'],route2=decoded2['coordinates'],route3=decoded3['coordinates'])