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


db = cliente ["nobel"]
prizes_collection = db["prizes"]



# Filtro a realizar en la consulta
filter = {}

# Conteo de documentos en una colección

num_prizes = db.prizes.count_documents(filter)

num_laureates = db.laureates.count_documents(filter)

# Seleccionamos un documento

doc = db.prizes.find_one(filter)	