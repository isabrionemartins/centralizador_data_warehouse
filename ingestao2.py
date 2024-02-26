
import pymongo 
from json import loads
host = "mongodb://localhost/"
port = 27017
conector = pymongo.MongoClient(host,port)
database = conector["sistema_mongo"]
categorias = database["categorias"]
produtos = database["produtos"]
with open("arquivos\\categorias.json","r") as file:
    categorias.insert_many(loads(file.read()))

with open("arquivos\\produtos.json","r") as file:
    produtos.insert_many(loads(file.read()))