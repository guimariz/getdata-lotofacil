import requests
import json
import urllib3
import time

http = urllib3.PoolManager()

def get_concurso(concurso):
  r = http.request(
      'GET',
      f'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/{concurso}',
      headers={'Content-Type': 'application/json'}
  )
  print(f'concurso {concurso} Check')
  data = json.loads(r.data.decode('utf-8'))
  resultado = sorted(data['dezenasSorteadasOrdemSorteio'])
  time.sleep(3)
  return {'numero_concurso': concurso, 'resultado': resultado}

concursos = [get_concurso(numero) for numero in range(2672, 2675)]

def write_file(file_name, todos):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(todos)
    file.close()

write_file('concursos.json', json.dumps(concursos))