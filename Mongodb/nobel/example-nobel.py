#conda install pymongo
from pymongo import MongoClient

# conda install -c conda-forge request
import requests
# Creamos la conexión a localhost por defecto
client = MongoClient()
# Creamos la base de datos nobel
db = client["nobel"]
# API https://www.nobelprize.org/about/developer-zone-2/
for collection_name in ["prizes","laureates"]:
	response = requests.get("http://api.nobelprize.org/v1/{}.json".format(collection_name[:-1]))
	# Convertimos los datos a Json
	documentos = response.json()[collection_name]
	db[collection_name].insert_many(documentos)


db = client ["nobel"]
prizes_collection = db["prizes"]



# Filtro a realizar en la consulta
filter = {}

# Conteo de documentos en una colección

num_prizes = db.prizes.count_documents(filter)
print ("Número de prizes: "+str(num_prizes))

num_laureates = db.laureates.count_documents(filter)
print ("Número de laureates: "+str(num_laureates))	
# Seleccionamos un documento

doc = db.prizes.find_one(filter)


print(doc)



# Listado del nombre de BB.DD.s
db_names = client.list_database_names()
print(db_names)

# Listado de colecciones que se encuentran en "nobel"
nobel_coll_names = client.nobel.list_collection_names()
print(nobel_coll_names)


# Recuperamos un elemento
prize = db.prizes.find_one()
laureate = db.laureates.find_one()


# Recuperamos los campos de cada documento
prize_fields = str(prize.keys())
laureate_fields = str(laureate.keys())

print(prize_fields)
print(laureate_fields)


# Filtro a realizar en la consulta
filter = {
	'diedCountry':'Germany'
}

resultado = db.laureates.count_documents(filter)
print ("Resultado "+str(resultado))


# Filtro a realizar en la consulta
filter = {
	'bornCountry':'Spain'
}

resultado = db.laureates.count_documents(filter)
print ("Resultado "+str(resultado))

resultado = db.laureates.find_one(filter)
print ("Resultado "+str(resultado))

filter = {'diedCountry':{
	'$in':['Spain','France']
}}

resultado = db.laureates.count_documents(filter)
print ("Resultado "+str(resultado))

resultado = db.laureates.find_one(filter)
print ("Resultado "+str(resultado))


resultado = db.laureates.count_documents({"born": {"$lt": "1800"}})
print ("Resultado "+str(resultado))