from flask import Flask,request,redirect,url_for
import json

app = Flask(__name__)

db = {}

@app.route('/graph', methods=['GET'])
def graph():
    return redirect(url_for('static', filename='graph.html'))


@app.route('/sensors',methods=['GET'])
def sensors():
    return json.dumps(list(db.keys())), 200 #prendo le chiavi del db, le metto in una lista e le trasformo in formato json per javascript


@app.route('/sensors/<s>',methods=['POST'])
def add_data(s):
    data = request.values['data']
    traffic = float(request.values['traffic volume'])
    if s in db:
        db[s].append((data,traffic))
    else:
        db[s] = [(data,traffic)]
    return 'ok',200

@app.route('/sensors/<s>',methods=['GET'])
def get_data(s):
    if s in db:
        # return json.dumps(db[s])
        r = []
        for i in range(len(db[s])):
            r.append([i, db[s][i][1]])
            #r.append([db[s][i][0],db[s][i][1]]) #nell'esempio del prof, al posto di db[s][i][0], c'era solo i, in modo tale da indicizzare gli elementi, senza mettere la data
        return json.dumps(r),200
    else:
        return 'sensor not found',404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) #host = '0.0.0.0' vuol dire che possono accedervi tutti, anche utenti esterni che non usano questo computer; la porta è 80. Quindi per accedere al server sul computer dovrò digitare l'url:"localhost:80" o solo "localhost" (questo nel caso in cui un endpoint è solo "\")
