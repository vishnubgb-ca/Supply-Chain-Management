import  pandas as pd
import pymysql
import os

def loading_data():
    #data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    hostname = os.environ["db_hostname"]
    print(hostname)
    username = os.environ["DB_USERNAME"]
    print(username)
    password = os.environ["DB_PASSWORD"]
    print(password)
    databasename = os.environ["DB_NAME"]
    print(databasename)
    connection = pymysql.connect(host=hostname, user=username,password=password,database=databasename)
    sql_query = "SELECT * FROM backorder_prediction"
    data = pd.read_sql(sql_query, connection)
    print(data)
    connection.close()
    return data

loading_data()
