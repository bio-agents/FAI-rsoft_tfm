import json
from pymongo import MongoClient

client = MongoClient()

with open('bioconductor2000.json', 'r') as infile:
    agents = json.load(infile)

db = client.FAIRsoft
testDB = db.test

def replaceDot(d):
    new = {}
    for k in d.keys():
        v = d[k]
        if isinstance(v, dict):
            v = replaceDot(d[k])
        new[k.replace('.', '-')] = v
    return new


for agent in agents:
    agent['integrated']=False
    agent = replaceDot(agent)
    #print(agent)
    testDB.insert_one(agent)
