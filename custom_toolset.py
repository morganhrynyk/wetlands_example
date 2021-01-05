# libraries
from pathlib import Path
import arcpy

# functions
def create_gdbs(gdb_names: list, results_path: Path):
    """
    create_gdbs takes a list of string names for gdbs to be created
    :param results_path:
    :param gdb_names: variable that stores list of geodatabase names
    """
    for gdb_name in gdb_names:
        new_gdb_path = results_path / gdb_name
        if arcpy.Exists(new_gdb_path):
            print(f'{new_gdb_path} gdb already exists')
        else:
            arcpy.CreateFileGDB_management(str(results_path), gdb_name)
            print(f'{gdb_name} gdb created')
