"""
Escrito por Jesús Omar Cuenca Espino 
A01378844@itesm.mx

25/03/2021
"""

import os
from shutil import rmtree

def createFolder(dirName : str):
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print(f"Folder {dirName} already Exists")

def deleteFolder(dirName : str):
    try:
        os.rmdir(dirName)
    except FileNotFoundError:
        print(f"Folder doesn't exist")
    except Exception as err:
        rmtree(dirName)

if __name__ == "__main__":
    import time
    TEST_DIR = "ExampleDir"
    createFolder(TEST_DIR)
    print("Folder Created")
    time.sleep(1)
    deleteFolder(TEST_DIR)
    print("Folder Deleted")
