from flask import Flask, request, json
from flask.wrappers import Response
from flask_cors import CORS
import comprobarArchivo
import a_apriori

app = Flask (__name__)

CORS(app)

@app.route('/uploadFile', methods=['POST'])
def uploadFile ():
    file = request.files['file']
    info = comprobarArchivo.comprobarArchivo(file)
    if   info == False:
        response = app.response_class(
            response=json.dumps(""),
            status=404,
            mimetype='application/json'
        )

    response = app.response_class(
            response=json.dumps(info),
            status=200,
            mimetype='application/json'
        )
    return response

@app.route('/apriori', methods=['POST'])
def apriori ():
    file = request.files['file']
    info = a_apriori.algoritmo(file)
    response = app.response_class(
            response=json.dumps("Hola"),
            status=200,
            mimetype='application/json'
        )
    return response

if __name__ == "__main__":
    app.run(debug=True)