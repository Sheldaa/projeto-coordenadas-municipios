import requests
import pandas as pd

API_KEY = 'Coloque aqui a chave da api do googlemaps'

df = pd.read_csv('municipios_dados.csv')

resultados = []

for municipio in df['Nomes']:
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={municipio},Ceará,Brazil&key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        resultados.append({
            'Municipio': municipio,
            'Latitude': location['lat'],
            'Longitude': location['lng']
        })
    else:
        print(f"Não foi possível buscar {municipio}: {data['status']}")
        resultados.append({
            'Municipio': municipio,
            'Latitude': 0,
            'Longitude': 0
        })

df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel('municipios_com_coordenadas.xlsx', index=False)


