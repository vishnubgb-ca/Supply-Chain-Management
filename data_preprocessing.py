import pandas as pd
from data_analysis import data_analysis
import numpy as np
from scipy import stats

def data_preprocess():
    data = data_analysis()
    data.drop(columns=["sku","lead_time"],axis=1,inplace=True)
    data = data.dropna(axis=0, how='any')
    df.replace(to_replace = -99, value = np.nan)
    df["perf_6_month_avg"] = df["perf_6_month_avg"].fillna(df["perf_6_month_avg"].median(), inplace=True)
    df["perf_12_month_avg"] = df["perf_12_month_avg"].fillna(df["perf_12_month_avg"].median(), inplace=True)
    print ("Missing values after removal of rows with empty values\n\n",data.isnull().any(),sep='')
    print(data)
    return data

data_preprocess()
