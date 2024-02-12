import  pandas as pd
import pymysql
import os

def loading_data():
    #data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    hostname = os.environ.get("DB_HOST_NAME")
    username = os.environ.get("DB_USER_NAME")
    password = os.environ.get("DB_PASSWORD")
    databasename = os.environ.get("DB_DB_NAME")
    #connection = pymysql.connect(host=hostname, user=username,password=password,database=databasename,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    connection = pymysql.connect(host='172.31.61.44', user='mlanglessyntacticai', password='mlanglessyntacticai123', database='syntactic_ai_pipelines_data')
    return data

loading_data()
