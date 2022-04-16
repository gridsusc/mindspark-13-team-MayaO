from pydoc import text
from flask import Flask, render_template
from flask import request
from flask import jsonify

import openrouteservice as ors

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mayaO'
client = ors.Client(key='5b3ce3597851110001cf624867c31029cd564d6d99171dbb0990af67') # Specify your personal API key
app.config["startGeoobject"] = None
app.config["destGeoobject"] = None

@app.route('/home', methods=['GET'])
def hello():
    return render_template("main.html")

@app.route('/searchstart', methods=['POST'])
def searchstart():
    data = request.form.get('startname')
    #call api to get start geojson => startgeo
    app.config["startGeoobject"] = getGeoCode(data)
    return jsonify(status="success", data=app.config["startGeoobject"]["features"][0]["properties"]["label"]) 

@app.route('/searchdest', methods=['POST'])
def searchdest():
    data = request.form.get('destname')
    #call api to get start geojson => destgeo
    app.config["destGeoobject"] = getGeoCode(data)
    return jsonify(status="success", data=app.config["destGeoobject"]["features"][0]["properties"]["label"])

def getGeoCode(searchstring):
    # print(dir(client))
    geoobject = client.pelias_search(text=searchstring,size=1)
    return geoobject

@app.route('/getpath', methods=['GET'])
def getpath():
    startcoords = (app.config["startGeoobject"]["features"][0]["geometry"]["coordinates"][0],app.config["startGeoobject"]["features"][0]["geometry"]["coordinates"][1])
    destcoords = (app.config["destGeoobject"]["features"][0]["geometry"]["coordinates"][0],app.config["destGeoobject"]["features"][0]["geometry"]["coordinates"][1])
    path1, path2, path3, routes = calculatepaths(startcoords,destcoords)
    return {"path1" : path1, "path2" : path2, "path3" : path3, "allroutes" : routes}
    

def calculatepaths(start,dest):
    #coords = ((8.54234,48.23424),(8.34423,48.26424))
    coords = (start,dest)
    routes  = client.directions(coords,alternative_routes={"share_factor":0.6,"target_count":3,"weight_factor":1.4})
    
    geometry1 = routes['routes'][0]['geometry']
    decoded1 = ors.convert.decode_polyline(geometry1)
    
    geometry2 = routes['routes'][1]['geometry']
    decoded2 = ors.convert.decode_polyline(geometry2)

    geometry3 = routes['routes'][2]['geometry']
    decoded3 = ors.convert.decode_polyline(geometry3)

    return decoded1,decoded2,decoded3, routes