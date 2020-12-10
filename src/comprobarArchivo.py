import pandas as pd
import os

def comprobarArchivo (file):

    extension = os.path.splitext(file.filename)[1]
    print(extension)
    info = ""
    #data.dropna(inplace = True) 
    try:
        if (extension == ".txt"):
            info = pd.read_table (file)
        elif (extension == ".cvs"):
            info = pd.read_cvs (file)
        elif (extension == ".xls" or extension == ".xlsx"):
            info = pd.read_excel (file)
        print (info.dtypes.to_string())
        toList (info.dtypes.to_string())
        info = " ".join(info.dtypes.to_string().split())
        return info
    except:
        print("error")
        return False
    

def toList (cadena):
    cadena_limpia = " ".join(cadena.split())
    #cadena_limpia = hola.replace('\n', ' ').replace('\r', '')
    #print(cadena_limpia)
    lista = cadena_limpia.split()
    print(lista)
    print("---")