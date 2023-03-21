# Author: Daniel Lopez Gala
import requests
import re
import json
import csv
import concurrent.futures

NUM_CONVOCATORIAS = 500000
#NUM_CONVOCATORIAS = 5000
NUM_ROWS = 200

MAX_WORKERS = 80

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.infosubvenciones.gob.es/bdnstrans/GE/es/convocatorias',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def download_convocatoria(page_num):
    url = f'https://www.infosubvenciones.gob.es/bdnstrans/busqueda?type=convs&_search=false&nd=1648563004804&rows=200&page={page_num}&sidx=0&sord=desc'
    response = requests.get(url, headers=headers, cookies=s.cookies)
    return response.text

print("[#] Obteniendo la respuesta del servidor.")
s = requests.session()
response = s.get('https://www.infosubvenciones.gob.es/bdnstrans/GE/es/convocatorias', headers=headers)

print("[i] Procesando las cookies y el token CSRF.")
csrf_token = re.search('<input type="hidden" name="_csrf" value="([^"]+)', response.text).group(1)

######

data = {
    'tipoBusqPalab': '1',
    'titulo': '',
    'strnumcov': '',
    'strmrr': '',
    'fecDesde': '',
    'fecHasta': '',
    'administracion': 'todo',
    '_otrosOrganos': '1',
    '_ministerios': '1',
    '_organos': '1',
    '_cAutonomas': '1',
    '_departamentos': '1',
    '_locales': '1',
    '_localesOculto': '1',
    '_regionalizacion': '1',
    '_idtipoben': '1',
    '_instrumentos': '1',
    'finalidad': '',
    'referencia': '',
    '_csrf': csrf_token,
}

print("[#] Utilizando el token CSRF para validar la JSESSIONID para las convocatorias.")
requests.post(
    'https://www.infosubvenciones.gob.es/bdnstrans/GE/es/convocatorias',
    headers=headers,
    data=data,
    cookies=s.cookies
)

#####
raw_convocatorias_data = []
print("[#] Obteniendo los datos de las convocatorias.")
downloads = 1
num_pages = (int) ((NUM_CONVOCATORIAS / NUM_ROWS) + ((NUM_CONVOCATORIAS % NUM_ROWS) > 0))
#with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
with concurrent.futures.ThreadPoolExecutor() as executor:
    res = [executor.submit(download_convocatoria, i) for i in range(num_pages)]
    for future in concurrent.futures.as_completed(res):
        response = future.result()
        print(f"[@] Completada la descarga número {downloads} de {num_pages}.")
        downloads += 1
        raw_convocatoria_data = response
        raw_convocatorias_data.append(raw_convocatoria_data)

"""
for i in range(num_pages):
    response = res[i].result()
    raw_convocatoria_data = response
    raw_convocatorias_data.append(raw_convocatoria_data)
"""

# %%
print("[i] Procesando los datos de las convocatorias.")


# Open a file for writing the CSV data
with open('convocatorias.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for raw_convocatoria_data in raw_convocatorias_data:
        # Parse the JSON data
        parsed_data = json.loads(raw_convocatoria_data)
        # Write each row of data
        rows = parsed_data['rows']
        if rows != None:
            for row in rows:
                csvwriter.writerow(row)

print("[i] Datos de las convocatorias procesados correctamente.")

# %%
import requests
import re
import json
import csv
import concurrent.futures

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.infosubvenciones.gob.es/bdnstrans/GE/es/concesiones',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

print("[#] Obteniendo la respuesta del servidor.")
s = requests.session()
response = s.get('https://www.infosubvenciones.gob.es/bdnstrans/GE/es/convocatorias', headers=headers)

print("[i] Procesando las cookies y el token CSRF.")
csrf_token = re.search('<input type="hidden" name="_csrf" value="([^"]+)', response.text).group(1)

######

data = {
    'tipoBusqPalab': '1',
    'titulo': '',
    'strnumcov': '',
    'strmrr': '',
    'fecDesde': '',
    'fecHasta': '',
    'administracion': 'todo',
    '_otrosOrganos': '1',
    '_ministerios': '1',
    '_organos': '1',
    '_cAutonomas': '1',
    '_departamentos': '1',
    '_locales': '1',
    '_localesOculto': '1',
    '_regionalizacion': '1',
    '_idtipoben': '1',
    '_instrumentos': '1',
    'finalidad': '',
    'referencia': '',
    '_csrf': csrf_token,
}

print("\n[#] Utilizando el token CSRF para validar la JSESSIONID para las concesiones.")
requests.post(
    'https://www.infosubvenciones.gob.es/bdnstrans/GE/es/concesiones',
    headers=headers,
    data=data,
    cookies=s.cookies
)

NUM_CONCESIONES = 18600000
NUM_CONCESIONES = 10000
NUM_ROWS = 200

def download_concesion(page_num):
    url = f'https://www.infosubvenciones.gob.es/bdnstrans/busqueda?type=concs&_search=false&nd=1648563004804&rows={NUM_ROWS}&page={page_num}&sidx=0&sord=desc'
    response = requests.get(url, headers=headers, cookies=s.cookies)
    return response.text

print("[#] Obteniendo los datos de las concesiones.")

raw_concesiones_data = []
downloads = 1
num_pages = (int) ((NUM_CONCESIONES / NUM_ROWS) + ((NUM_CONCESIONES % NUM_ROWS) > 0) + 1)
#with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
    res = [executor.submit(download_concesion, i) for i in range(1, num_pages)]
    for future in concurrent.futures.as_completed(res):
        response = future.result()
        print(f"[@] Completada la descarga número {downloads} de {num_pages}.")
        downloads += 1
        raw_concesion_data = response
        raw_concesiones_data.append(raw_concesion_data)

# %%
print("[i] Procesando los datos de las concesiones.")

# Open a file for writing the CSV data
with open('concesiones.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    #print("Número de descargas: ", len(raw_convocatorias_data))
    for raw_concesion_data in raw_concesiones_data:
        # Parse the JSON data
        parsed_data = json.loads(raw_concesion_data)
        # Write each row of data
        rows = parsed_data['rows']
        if rows != None:
            for row in rows:
                csvwriter.writerow(row)

print("[i] Datos de las concesiones procesados correctamente.")


