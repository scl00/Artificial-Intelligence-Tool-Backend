import numpy as np 
import pandas as pd 
from apyori import apriori
import os


def algoritmo (file):
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
        else:
            return False
        registros = []
        print(info.size())
        # for i in range (0, )

        print (info.dtypes.to_string())
        info = " ".join(info.dtypes.to_string().split())
        return info
    except:
        print("a error")
        return False