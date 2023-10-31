"""
This is a script that loads in data from either CSV, JSON, XML or TXT files
and then saves it to a variable. If the parameter pandas is True then the data is saved as a pandas dataframe.

Created by: Mathias Herl'v Lund
Date: 31/10/2023
Version: 1.0

"""

import csv
import json
import sqlite3
import sys
import pandas as pd

def load_data(file_name, file_type, dataname,pandas=False):
    case = file_type.lower()
    if pandas == True:
        #Load in the data as a pandas dataframe
        if case == "csv":
            dataname = pd.read_csv(file_name)
        elif case == "json":
            dataname = pd.read_json(file_name)
        elif case == "xml":
            dataname = pd.read_xml(file_name)
        elif case == "txt":
            dataname = pd.read_txt(file_name)
        else:
            print("File type not supported")
            sys.exit()
    if case == "csv":
        # Open the file and read it
        csvfile = open(file_name, 'r')
        reader = csv.reader(csvfile, delimiter=',')
        #Then save it as dataname
        dataname = []
        for row in reader:
            dataname.append(row)
        csvfile.close()  
    elif case == "json":
        #Open the file and read it
        jsonfile = open(file_name, 'r')
        jsondata = json.load(jsonfile)
        #Then save it as dataname
        dataname = []
        for row in jsondata:
            dataname.append(row)
        jsonfile.close()
        
    elif case == "xml":
        #Open the file and read it
        xmlfile = open(file_name, 'r')
        xmldata = xmlfile.read()
        #Then save it as dataname
        dataname = []
        for row in xmldata:
            dataname.append(row)
        xmlfile.close()
        
    elif case == "txt":
        #Open the file and read it
        txtfile = open(file_name, 'r')
        txtdata = txtfile.read()
        #Then save it as dataname
        dataname = []
        for row in txtdata:
            dataname.append(row)
        txtfile.close()
        

    else:
        print("File type not supported")
        sys.exit()
    return dataname


