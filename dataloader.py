"""
This is a script that loads in data from either CSV or TXT files
and then saves it to a variable. If the parameter pandas is True then the data is saved as a pandas dataframe.

Created by: Mathias Herløv Lund
Date: 31/10/2023
Version: 1.0

"""

import csv
import sys
import pandas as pd
import numpy as np

def load_data(file_name, file_type, dataname, pandas=False,numpy=False):
    case = file_type.lower()
    if pandas:
        if case == "csv":
            try:
                dataname = pd.read_csv(file_name)
            except Exception as e:
                print(f"Error: An error occurred while loading the file {file_name}.")
                print(f"Details: {str(e)}")
                dataname = None
        elif case == "txt":
            #load in txt file
            dataname = pd.read_csv(file_name, delimiter=" ")
            return dataname
        else:
            print("File type not supported")
            return None
    elif pandas == False:
        if case == "csv":
            with open(file_name, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                dataname = [row for row in reader]
        elif case == "txt":
            #load in txt file
            dataname = pd.read_csv(file_name, delimiter=" ")
            return dataname
        else:
            print("File type not supported")
            return None
    return dataname
