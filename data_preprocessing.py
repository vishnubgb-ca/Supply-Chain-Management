import pandas as pd
from data_analysis import data_analysis
import numpy as np
from sklearn.preprocessing import LabelEncoder
from scipy import stats

def data_preprocess():
    data = data_analysis()
    data = data.drop(columns=["sku","lead_time"],axis=1)
    data = data.dropna(axis=0, how='any')
    data = data.replace(to_replace = -99, value = np.nan)
    data["perf_6_month_avg"] = data["perf_6_month_avg"].fillna(data["perf_6_month_avg"].median())
    data["perf_12_month_avg"] = data["perf_12_month_avg"].fillna(data["perf_12_month_avg"].median())
    print ("Missing values after removal of rows with empty values\n\n",data.isnull().any(),sep='')
    print(data)
    le=LabelEncoder()
    
    data['potential_issue']=le.fit_transform(data['potential_issue'])
    data['deck_risk']=le.fit_transform(data['deck_risk'])
    data['oe_constraint']=le.fit_transform(data['oe_constraint'])
    data['ppap_risk']=le.fit_transform(data['ppap_risk'])
    data['stop_auto_buy']=le.fit_transform(data['stop_auto_buy'])
    data['rev_stop']=le.fit_transform(data['rev_stop'])
    data['went_on_backorder']=le.fit_transform(data['went_on_backorder'])
    #names=["national_inv",	"in_transit_qty",	"forecast_3_month",	"forecast_6_month"	,"forecast_9_month"	,"sales_1_month", "sales_3_month", "sales_6_month", "sales_9_month", "min_bank", "pieces_past_due", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    #outlier detection
    #for i,j in enumerate(names):
    #    plt.figure(figsize=(12,15))
    #    plt.subplot(8,5,i+1)
    #    sns.boxplot(y=j,data=data)

    return data

data_preprocess()
