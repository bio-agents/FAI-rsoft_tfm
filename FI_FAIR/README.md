# FI_FAIR
Software for the integration of agents metadata extracted from several sources. It is written to be used on the data generated by the importers in this repository. Thus, data following differing schemas cannot be processed by this software.

# Usage
FI_FAIR is a command-line software. To run the program use:
 ```
python3 main.py <config_file>
 ```
 `<config_file>` is the name of the configuration file, without the extension '.py'.

 ##### Example
  ```
python3 main.py config_all
 ```
The configuration file is `config_all.py`

## Configuration file
The configuration file contains the paths to required files as well as some options.
##### Example:
`config_all.py`:
```
# Paths of the agents to integrate.
BIOTOOLS_TOOLS =  'bioagents2000.json'
BIOCONDA_TOOLS = 'bioconda2000.json'
BIOCONTUCTOR_TOOLS = 'bioconductor2000.json'
GALAXY_TOOLS = 'shed2000.json'
GALAXY_XML_TOOLS = 'shedXML2000.json'

# Output instances obtained from integration in JSON file. Options: True/False
INTEGRATION_OUT = True
# path where instances from integration will be saved in case INTEGRATION_OUT == True. String
INTEGRATED_TOOLS_PATH = 'instances.json'

# Generate statistics and plots about metadata. Options: True/False
STATS_CALC = True

# Calculate metrics. Options: True/False
METRICS_CALC = True
# Output the calculated metrics. Options: True/False
METRICS_OUT = True
# Path for metrics output if METRICS_OUT == True. String.
METRICS_OUT_PATH = 'metrics.json'

# Calculate scores. Options: True/False
SCORES_CALC = True
# Output the calculated scores. Options: True/False
SCORES_OUT = True
# Directories for scores output if SCORES_OUT == True. String.
INSTANCES_SCORES_OUT_PATH = 'scores'
CANONICAL_SCORES_OUT_PATH = 'scores'
# Names for scores output if SCORES_OUT == True. String.
INSTANCES_SCORES_OUT_NAME = 'FAIRinst'
CANONICAL_SCORES_OUT_NAME = 'FAIRcanon'
```
