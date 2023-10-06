import  pandas as pd

def loading_data():
    data = pd.read_csv('./Kaggle_Test_Dataset_v2.csv')
    return data

loading_data()