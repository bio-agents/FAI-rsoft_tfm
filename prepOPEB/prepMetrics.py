import json


typesMap = {'Command-line agent':'cmd',
    'Web application':'web',
    'Library':'lib',
    'Desktop application':'app',
    'Database portal':'db',
    'Web service':'soap',
    'Web API':'rest',
    'Suite':'suite',
    'Script':'script',
    'Workbench':'workbench',
    'Plug-in':'plugin',
    'Workflow':'workflow',
    'SPARQL endpoint':'sparql',
    'None': 'None'
    }


rawScores = open('scores/FAIRinsts.txt', 'r')
Scores ={}

for line in rawScores:
    line = line.strip()
    fields = line.split('\t')
    Scores[fields[0]] = [float(fields[1]), float(fields[2]), float(fields[3]), float(fields[4])]



with open('metrics.json', 'r') as infile:
    rawMetrics = json.load(infile)
'''
from pymongo import MongoClient
client = MongoClient()
db = client.FAIRmetrics
collection = db.metrics
'''
Metrics = []
for agent in rawMetrics:
    #print(agent['name'])
    #print(agent['version'])
    #print(agent['type'])

    if agent['version']:
        version = agent['version']
    else:
        version = 'None'
    if agent['type']:
        type_ = agent['type']
    else:
        type_ = 'None'

    ID = agent['name'] + '/' + version + '/' + type_
    id_ = agent['name'] + '/' + version + '/' + typesMap[type_]

    metrics = { 'id' : id_ ,
    'F' : {'1. Identity uniqueness':{'1.1. Uniqueness of name': agent['F1_1'],'1.2. Identifiability of version': agent['F1_2'] },
            '2. Existence of Metadata': {'2.1. Structured Metadata': agent['F2_1'], '2.2. Standarized Metadata': agent['F2_2']},
            '3. Searchability': {'3.1. Searchability in registries': agent['F3_1'] ,'3.2. Searchability in software repositories': agent['F3_2'], '3.3. Searchability in literature': agent['F3_3'] }  },
    'A': {'1. Existance of downloadable, buildable or accesible working version':{'1.1. Existence of API or web': agent['A1_1'], '1.2. Existence of downloadable and buildable software working version':agent['A1_2'] ,'1.3. Existence of installation instructions':agent['A1_3'], '1.4. Existence of test data':agent['A1_4'], '1.5. Existence of software source code':agent['A1_5'] },
          '2. Software history trackability': {'2.1. Metadata of previous versions at software repositories':agent['A2_1'], '2.2. Existence of accesible previous versions of the software':agent['A2_2']},
          '3. Restricted access': {'3.1. Registration compulsory':agent['A3_1'], '3.2. Availability of version for free software':agent['A3_2'], '3.3. Availability for several OS':agent['A3_3'], '3.4. Availability on free e-infrastructure':agent['A3_4'], '3.5. Availability on several e-infrastructures':agent['A3_5']} },
    'I': {
        '1. Documentation on input/output datatypes and formats': {'1.1. Usage of standard data formats':agent['I1_1'], '1.2. Usage of standard API framework':agent['I1_2'], '1.3. Verificability of data formats':agent['I1_3'], '1.4. Flexibility of data format supported':agent['I1_4'], '1.5. Generation of provenance information':agent['I1_5'] },
        '2. Workflow compatibility': {'2.1. Existence of of API/library version':agent['I2_1'], '2.2. E-infrastructure compatibility':agent['I2_2']},
        '3. Dependencies availability': {'3.1. Dependencies statement':agent['I3_1'], '3.2. Dependencies are provided':agent['I3_2'], '3.3. Availability through dependencies aware systems':agent['I3_3']}},
    'R': {'1. Existence of usage documentation' : {'1.1. Existence of usage guides':agent['R1_1'], '1.2. Existence of conditions of use':agent['R1_2']},
        '2. Existence of License': {'2.1. Existence of terms of use':agent['R2_1'], '2.2. Existence of conditions of use':agent['R2_2']},
        '3. Existence of contribution policy': {'3.1. Contributors policy specification':agent['R3_1'], '3.2. Existence of credit': agent['R3_2']},
        '4. Provenance availability': {'4.1. Usage of version control':agent['R4_1'], '4.2. Existence of release policy': agent['R4_2'], '4.3. Metadata of previous versions at software repositories':agent['R4_3']}},
    'scores': Scores[ID],
    'type': typesMap[type_],
    'version': version,
    'name': agent['name']
    }
    Metrics.append(metrics)
    #collection.insert_one(metrics)

'''
'F' : {'1':{'1': agent['F1_1'],'2': agent['F1_2'] },
        '2': {'1': agent['F2_1'], '2': agent['F2_2']},
        '3': {'1': agent['F3_1'] ,'2': agent['F3_2'], '3': agent['F3_3'] }  },
'A': {'1':{'1': agent['A1_1'], '2':agent['A1_2'] ,'3':agent['A1_3'], '4':agent['A1_4'], '5':agent['A1_5'] },
      '2': {'1':agent['A2_1'], '2':agent['A2_2']},
      '3': {'1':agent['A3_1'], '2':agent['A3_2'], '3':agent['A3_3'], '4':agent['A3_4'], '5':agent['A3_5']} },
'I': {
    '1': {'1':agent['I1_1'], '2':agent['I1_2'], '3':agent['I1_3'], '4':agent['I1_4'], '5':agent['I1_5'] },
    '2': {'1':agent['I2_1'], '2':agent['I2_2']},
    '3': {'1':agent['I3_1'], '2':agent['I3_2'], '3':agent['I3_3']}},
'R': {'1' : {'1':agent['R1_1'], '2':agent['R1_2']},
    '2': {'1':agent['R2_1'], '2':agent['R2_2']},
    '3': {'1':agent['R3_1'], '2': agent['R3_2']},
    '4': {'1':agent['R4_1'], '2': agent['R4_2'], '3':agent['R4_3']}},
'scores': Scores[ID],
'''


with open('metrics_OPEB.json', 'w') as outfile:
    json.dump(Metrics, outfile)
