import os
import pathlib

path = (str(pathlib.Path(__file__).resolve().parent ) )
list =  [ print(f"{file[0]} : {file[1]}") for file in enumerate ( (os.listdir(path)) , 1 ) ]

# print(list)