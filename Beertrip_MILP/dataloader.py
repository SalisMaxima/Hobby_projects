"""
This is a script that loads in data from either CSV, JSON, XML or TXT files
and then saves it to a database.

Created by: Mathias Herl'v Lund
Date: 31/10/2023
Version: 1.0

"""

import csv,pandas as pd, json, xml.etree.ElementTree as ET, sqlite3, os, sys, time

def load_data(file_name, file_type, db_name, table_name):
    case = file_type.lower()
    if case == "csv":
        database = csv_to_db(file_name, db_name, table_name)
    elif case == "json":
        database = json_to_db(file_name, db_name, table_name)
    elif case == "xml":
        database = xml_to_db(file_name, db_name, table_name)
    elif case == "txt":
        database = txt_to_db(file_name, db_name, table_name)
    else:
        print("File type not supported")
        sys.exit()

def csv_to_db(file_name, db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name, ', '.join(['{} TEXT'.format(h) for h in headers]))
        c.execute(query)
        for row in reader:
            query = 'INSERT INTO {} VALUES ({})'.format(table_name, ', '.join(['?' for _ in headers]))
            c.execute(query, row)
    conn.commit()
    conn.close()
    # return the database connection object
    return conn

def json_to_db(file_name, db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    with open(file_name, 'r') as f:
        data = json.load(f)
        headers = list(data[0].keys())
        query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name, ', '.join(['{} TEXT'.format(h) for h in headers]))
        c.execute(query)
        for row in data:
            values = [row[h] for h in headers]
            query = 'INSERT INTO {} VALUES ({})'.format(table_name, ', '.join(['?' for _ in headers]))
            c.execute(query, values)
    conn.commit()
    conn.close()
    # return the database connection object
    return conn

def xml_to_db(file_name, db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    tree = ET.parse(file_name)
    root = tree.getroot()
    headers = list(set([child.tag for child in root]))
    query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name, ', '.join(['{} TEXT'.format(h) for h in headers]))
    c.execute(query)
    for child in root:
        values = [child.find(h).text for h in headers]
        query = 'INSERT INTO {} VALUES ({})'.format(table_name, ', '.join(['?' for _ in headers]))
        c.execute(query, values)
    conn.commit()
    conn.close()
    # return the database connection object
    return conn

def txt_to_db(file_name, db_name, table_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    with open(file_name, 'r') as f:
        lines = f.readlines()
        headers = lines[0].strip().split(',')
        query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name, ', '.join(['{} TEXT'.format(h) for h in headers]))
        c.execute(query)
        for line in lines[1:]:
            values = line.strip().split(',')
            query = 'INSERT INTO {} VALUES ({})'.format(table_name, ', '.join(['?' for _ in headers]))
            c.execute(query, values)
    conn.commit()
    conn.close()
    # return the database connection object
    return conn



