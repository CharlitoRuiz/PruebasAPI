import requests

url = "https://api.deezer.com/search?q=artist:\"slipknot\""

payload = {}
headers = {
  'Cookie': 'dzr_uniq_id=dzr_uniq_id_fr066ce0c22f0e4d04a783bca3ea03a6a160065a'
}

response = requests.request("GET", url, headers=headers, data = payload)

#print(response.text.encode('utf8'))


def test_validar_que_el_codigo_de_respuesta_sea_200():
  response = requests.get(url)
  pResponseCode = response.status_code
  print("{}{}".format("El codigo de respuesta del API es: ", pResponseCode))
  assert response.status_code == 200

def test_validar_el_tipo_de_header():
  response = requests.get(url)
  pResponse = response.headers['Content-Type']
  print("{}{}".format("El header de la API es: ", pResponse))
  assert response.headers['Content-Type'] == "application/json; charset=utf-8"


def test_validar_que_la_cancion_uno_sea_psycosocial():
  response = requests.get(url)
  response_body = response.json()
  pResponse = response_body['data'][0]['title']
  print("{}{}".format("El titulo que se devuelve es: ", pResponse))
  assert pResponse == "Psychosocial"
