from requests import get, post #librerie http per l'utilizzo di funzioni get e post
import time

base_url = 'http://localhost:80'
sensor = 's1'
with open('Banglore_traffic_Dataset_100_5_numeri.csv') as f:
    for l in f.readlines()[1:]:
        data,traffic = l.strip().split(',') #leggo solo i valori della data e dell'area
        print(data,traffic)
        r = post(f'{base_url}/sensors/{sensor}',
                 data={'data':data,'traffic volume':traffic}) #posto su questo url, questi valori
        time.sleep(5) #posto i valori ogni 5 secondi

print('done')