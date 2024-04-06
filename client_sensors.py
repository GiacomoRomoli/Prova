from requests import get, post
import time

#base_url = 'http://34.154.157.58:80'
base_url = 'http://localhost'
sensor = 's1'
with open('CleanData_PM10.csv') as f: #vado a leggere il file csv, simulando l'arrivo di dati da parte di un sensore, per poi prendere questi dati e caricarli sul server
    for l in f.readlines()[1:]: #salto la prima riga perché è quella di intestazione
        data,val = l.strip().split(',')
        print(data,val)
        r = post(f'{base_url}/sensors/{sensor}',
                 data={'data':data,'val':val}) #mando il valore 'val', alla data 'data', al sensore 'sensor'
        time.sleep(5)



print('done')
