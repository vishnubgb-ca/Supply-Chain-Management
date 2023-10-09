import pandas as pd
from data_analysis import data_analysis
import numpy as np
from scipy import stats

def data_preprocess():
    data = data_analysis()
    data.drop(columns=["sku","lead_time"],axis=1,inplace=True)
    data = data.dropna(axis=0, how='any')
    print ("Missing values after removal of rows with empty values\n\n",data.isnull().any(),sep='')
    print(data)
    return data

data_preprocess()
