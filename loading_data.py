import  pandas as pd
import pymysql
import os

def loading_data():
    #data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    hostname = os.getenv("DB_HOST_NAME")
    print(hostname)
    username = os.getenv("DB_USER_NAME")
    print(username)
    password = os.getenv("DB_PASSWORD")
    print(password)
    databasename = os.getenv("DB_DB_NAME")
    print(databasename)
    connection = pymysql.connect(host='172.31.61.44', user=username,password=password,database=databasename,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    sql_query = "SELECT * FROM backorder_prediction"
    data = pd.read_sql(sql_query, connection)
    connection.close()
    return data

loading_data()
