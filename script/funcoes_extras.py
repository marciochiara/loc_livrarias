import pandas as pd

def excel_para_csv(caminho_excel, caminho_csv, separador):
  ''' Função para conversão de um arquivo em excel para um csv.'''
    df = pd.read_excel(caminho_excel)
    df.to_csv(caminho_csv, sep=separador, index=False)

# Exemplo de uso
#caminho_excel = r'C:\Users\arquivo.xlsx'  
#caminho_csv = r'C:\Users\arquivo.csv'  
#separador = ';' 

#excel_para_csv(caminho_excel, caminho_csv, separador)


def getGeoCoord(address):
    ''' Função para chamada da API de Geocoding do Google'''
    params = {
        'key': API_KEY,
        'address': address.replace(' ', '+')
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        return location['lat'], location['lng']
    else:
        return 'erro'

  #API_KEY = 'bla bla bla'

# Chamada da API
start_time = time.time()

erros = []

for i in range(df2.shape[0]):
    temp = time.time()
    
    # Método anterior
    try:
        df2.loc[i,'long'], df2.loc[i,'lat'] = getGeoCoord(df2.loc[i,'endereco'])
    except:
        erros.append(getGeoCoord(df2.loc[i,'endereco']))

    print(i,"--- %s seconds ---" % (time.time() - temp))
    
print("--- %s seconds ---" % (time.time() - start_time))
