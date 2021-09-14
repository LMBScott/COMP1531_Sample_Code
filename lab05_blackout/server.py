from flask import Flask, request
from json import dumps
import blackout

app = Flask(__name__)

@app.route('/city', methods=['POST'])
def addCity():
    city = request.get_json()
    blackout.cities.append(city)
    return dumps({
    })

@app.route('/satellite', methods=['POST'])
def addSatellite():
    satellite = request.get_json()
    blackout.satellites.append(satellite)
    return dumps({
    })

@app.route('/simulate', methods=['GET'])
def simulate():
    simOutput = blackout.simulate()
    return dumps({
        'cities' : simOutput
    })

if __name__ == '__main__':
    app.run(port=0)
