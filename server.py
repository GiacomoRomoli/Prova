from flask import Flask,request,redirect,url_for #flask è una libreria che permette di creare applicazioni web
import json
from joblib import load

app = Flask(__name__) #creo un'applicazione

db = {}

#devo andare a creare una cartella 'static' all'interno della quale vado ad inserire, oltre agli asset e le immagini che mi servono per la pagina web, il file html (che è un file statico, non è interattivo come un javascript o un python). Questo perché se lo tenessi all'interno della cartella dove stanno anche tutti gli altri file di python mi darebbe errore. Questo succede perché il server che mi ha fornito questa pagina web e il server che mi fornisce i dati sono su due server diversi, dunque il browser decide di bloccare la richiesta per problemi di privacy.
@app.route('/graph')
def graph():
    return redirect(url_for('static', filename='graph.html')) #quando andrò all'url /graph, allora verrò ricondotto alla cartella 'static', al file 'graph.html'



@app.route('/sensors',methods=['GET'])
def main():
    return json.dumps(list(db.keys())), 200


@app.route('/sensors/<s>',methods=['POST'])
def add_data(s):
    data = request.values['data']
    val = float(request.values['val'])
    if s in db:
        db[s].append((data,val))
    else:
        db[s] = [(data,val)]
    return 'ok',200

@app.route('/sensors/<s>',methods=['GET'])
def get_data(s):
    if s in db:
        #return json.dumps(db[s])
        r = []
        for i in range(len(db[s])):
            r.append([i,db[s][i][1]]) #vado a prendere il valore da un dizionario che è una lista di liste

        model = load('model.joblib')
        yp = model.predict([[r[-1][1],r[-2][1],r[-3][1],0]])
        r.append([len(db[s]),yp[0]])
        return json.dumps(r),200
    else:
        return 'sensor not found',404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) #faccio partire un'applicazione web

