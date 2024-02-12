import  pandas as pd
import pymysql
import os

def loading_data():
    #data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    hostname = os.environ.get("DB_HOST_NAME")
    username = os.environ.get("DB_USER_NAME")
    password = os.environ.get("DB_PASSWORD")
    databasename = os.environ.get("DB_DB_NAME")
    connection = pymysql.connect(host=hostname, user=username,password=password,database=databasename,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    sql_query = "SELECT * FROM backorder_prediction"
    data = pd.read_sql(sql_query, connection)
    connection.close()
    return data

loading_data()
