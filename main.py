import csv # Para trabajar con la base de datos

# Formato de los datos:
# \ufeffregister_id,direction,origin,destination,year,date,product,transport_mode,company_name,total_value

# Leer el archivo y almacenarlo en la variable datos
with open("synergy_logistics_database.csv", "r") as archivo:
  lector = csv.DictReader(archivo)
  base_datos = []
  for linea in lector:
   base_datos.append(linea)

#definir una función que agrupa y ordena los datos
def filtrar_ordenar(datos,tipo,indice):
  """
  Argumentos:
  - datos: Lista donde se guardan los diccionarios con los datos de las operaciones
  - tipo: El tipo de operación (importación o exportación) 
  - indice: Criterio para ordenar los datos (2 para la cantidad de rutas, 3 para el monto total por ruta)
  """
  conteo = []
  contados = []
  total = 0
  for operacion in datos:
    total += int(operacion['total_value'])
  for dato in lista:
    if dato['direction'] == tipo and ([dato['origin'], dato['destination']] not in contados):
      cantidad = 0
      monto = 0
      for operacion in datos:
        if [dato['origin'],dato['destination']] == [operacion['origin'],operacion['destination']]:
          cantidad += 1
          monto += int(operacion['total_value'])
      contados.append([dato['origin'], dato['destination']])
      conteo.append([dato['origin'], dato['destination'], cantidad, monto, monto / total ])
  conteo.sort(key = lambda dato: dato[indice], reverse = True)
  return conteo

def filtrar_ordenar_transp(datos, indice):
  """
  Filtra y ordena los transportes usados de acuerdo con el criterio especificado en el argummento índice (2 para la cantidad de rutas que usan ese transporte, 3 para el monto total por transporte)
  """
  conteo = []
  contados = []
  total = 0
  for operacion in datos:
    total += int(operacion['total_value'])
  for dato in datos:
    if dato['transport_mode'] not in contados:
      cantidad = 0
      monto = 0
      for operacion in datos:
        if dato['transport_mode'] == operacion['transport_mode']:
          cantidad += 1
          monto += int(operacion['total_value'])
      contados.append(dato['transport_mode'])
      conteo.append([dato['transport_mode'], cantidad, monto, monto / total ])
  conteo.sort(key = lambda dato: dato[indice], reverse = True)
  return conteo


# exp_rutas = filtrar_ordenar(datos,'Exports',2)
# imp_rutas = filtrar_ordenar(datos,'Imports',2)
# exp_monto = filtrar_ordenar(datos,'Exports',3)
# imp_monto = filtrar_ordenar(datos,'Imports',3)
#trans_monto = filtrar_ordenar_transp(base_datos, 3)
#trans_cant = filtrar_ordenar_transp(base_datos, 2)
