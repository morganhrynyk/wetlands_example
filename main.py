# libraries
from pathlib import Path
import arcpy
from wetlands_example import \
    custom_toolset as ct

# GLOBAL VARIABLES
# path variables
WORKING_DIR_PATH = Path.cwd()  # current working directory ie. where the script lives
print(WORKING_DIR_PATH)
RESULTS_DIR_PATH = WORKING_DIR_PATH / 'results_directory'  # root directory --> where GLPI wetlands data is stored on computer
print(RESULTS_DIR_PATH)
# input variables
GDB_NAMES = ['enney', 'meeny', 'miney', 'mo']

# call function
ct.create_gdbs(gdb_names=GDB_NAMES, results_path=RESULTS_DIR_PATH)
