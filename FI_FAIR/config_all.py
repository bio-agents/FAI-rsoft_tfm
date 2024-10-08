# Paths of the agents to integrate.
BIOTOOLS_TOOLS =  'bioagents2000.json'
BIOCONDA_TOOLS = 'bioconda2000.json'
BIOCONTUCTOR_TOOLS = 'bioconductor2000.json'
GALAXY_TOOLS = 'shed2000.json'
GALAXY_XML_TOOLS = 'shedXML2000.json'

# Instances obtained from integration writen as json
INTEGRATION_OUT = True
# path where instances from integration will be saved if INTEGRATION_OUT == True.
INTEGRATED_TOOLS_PATH = "instances.json"

# Statistics and plots about metadata
STATS_CALC = True

# Metrics ans scores calculated
METRICS_CALC = True
METRICS_OUT = True
METRICS_OUT_PATH = 'metrics.json'

SCORES_CALC = True
SCORES_OUT = True
INSTANCES_SCORES_OUT_PATH = 'scores'
INSTANCES_SCORES_OUT_NAME = 'FAIRinst'
CANONICAL_SCORES_OUT_PATH = 'scores'
CANONICAL_SCORES_OUT_NAME = 'FAIRcanon'
