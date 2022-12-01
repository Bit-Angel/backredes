from sys import int_info
from gevent import monkey
monkey.patch_all()
from flask import Flask, jsonify, request
from flask.json import JSONDecoder
from werkzeug.wrappers import Response, response
from flask_socketio import SocketIO, join_room, leave_room
from flask_cors import CORS
import json
#import socketio
####Imports de los archivos principales
import BackEnd.generalInfo.ResponseMessages as ResponseMessages
import BackEnd.FunctionsIO  as callMethod


usersConnected = {}

users = {
    "betomper@gmail.com": "qwerty",
    "prueba@gmail.com": "prueba123",
    "hola@gmail.com": "hola123"
}

app = Flask(__name__)
CORS(app)
#manage_session para poder utilizar sockets y apis
socketio = SocketIO(app, cors_allowed_origins="*", manage_session=False, async_mode='gevent')
#sio = socketio.Server()
#app = socketio.WSGIApp(socketio)
#enviroment = config['development']
#app = create_app(enviroment)


@app.route('/apiGet/<strId>', methods=['GET'])
def ApiGet(strId):
    try:
        print("apiGet StrId: ",strId)
        print("ip2: ",request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr))
        return jsonify({'data':{'status': 'succes'}})
    except Exception as exception:
        print('functionApiGet', exception)
        return jsonify({'intResponse':'500','strAnswer':'Server Error.'})
    
@app.route('/api/general/setDesaparecido', methods=['POST'])
def setDesaparecido():
    try:
        print(request.json)
        nombre = None if request.json['nombre'] == None else request.json['nombre']
        primape = None if request.json['primape'] == None else request.json['primape']      
        segape = None if request.json['segape'] == None else request.json['segape']      
        pais = None if request.json['pais'] == None else request.json['pais']      
        estado = None if request.json['estado'] == None else request.json['estado']      
        claveEntidad = None if request.json['claveEntidad'] == None else request.json['claveEntidad']      
        municipio = None if request.json['municipio'] == None else request.json['municipio']      
        origen = None if request.json['origen'] == None else request.json['origen']      
        nacionalidad = None if request.json['nacionalidad'] == None else request.json['nacionalidad']     
        sexo = None if request.json['sexo'] == None else request.json['sexo']      
        fecha_nac = None if request.json['fecha_nac'] == None else request.json['fecha_nac']      
        visto_ultima = None if request.json['visto_ultima'] == None else request.json['visto_ultima']      
        autoridad = None if request.json['autoridad'] == None else request.json['autoridad']      
        coordenadaX = None if request.json['coordenadaX'] == None else request.json['coordenadaX']      
        coordenadaY = None if request.json['coordenadaY'] == None else request.json['coordenadaY']      

        jsonResponse = callMethod.fnSetDesaparecido(nombre,primape,segape,pais,estado,claveEntidad,municipio,origen,nacionalidad,sexo,fecha_nac,visto_ultima,autoridad,coordenadaX,coordenadaY)
        return jsonify(jsonResponse)
    except Exception as exception:
        print('updateMonth', exception)
        return ResponseMessages.err202

      
@app.route('/api/general/getDesaparecido/<id>', methods=['GET'])
def getDesaparecido(id):
    try:
        jsonResponse = callMethod.getDesaparecido(id)
        print(jsonResponse)
        return jsonify(jsonResponse)
    except Exception as exception:
        print('updateMonth', exception)
        return ResponseMessages.err202

@app.route('/api/general/getDoctorByEmailAndPass/<email>/<password>', methods=['GET'])
def getDoctorByEmailAndPass(email,password):
    try:
        jsonResponse = callMethod.fnGetDoctorByEmailAndPass(email,password)
        print(jsonResponse)
        return jsonify(jsonResponse)
    except Exception as exception:
        print('updateMonth', exception)
        return ResponseMessages.err202
    
@app.route('/api/general/getEst_Doc', methods=['GET'])
def getEst_Doc():
    try:
        jsonResponse = callMethod.fnGetEst_Doc()
        print(jsonResponse)
        return jsonify(jsonResponse)
    except Exception as exception:
        print('updateMonth', exception)
        return ResponseMessages.err202

@app.route('/api/general/getCitasUsuario/<idUser>', methods=['GET'])
def getCitasUsuario(idUser):
    try:
        jsonResponse = callMethod.fnGetCitasUsuario(idUser)
        print(jsonResponse)
        return jsonify(jsonResponse)
    except Exception as exception:
        print('updateMonth', exception)
        return ResponseMessages.err202
    
@app.route('/api/general/getCitasDoctor/<idDoc>', methods=['GET'])
def getCitasDoctor(idDoc):
    try:
        jsonResponse = callMethod.fnGetCitasDoctor(idDoc)
        print(jsonResponse)
        return jsonify(jsonResponse)
    except Exception as exception:
        print('updateMonth', exception)
        return ResponseMessages.err202
    
if __name__ == '__main__':
   socketio.run(app, host="0.0.0.0", port=6007, debug=True)
# #if __name__ == '__main__':
   #socketio.run(app, host="192.168.0.4", port=6007, debug=True)

