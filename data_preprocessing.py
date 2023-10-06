import pandas as pd
from loading_data import loading_data
import numpy as np
from scipy import stats

def data_preprocess():
    data = loading_data()
    names=["national_inv",	"in_transit_qty",	"forecast_3_month",	"forecast_6_month"	,"forecast_9_month"	,"sales_1_month", "sales_3_month", "sales_6_month", "sales_9_month", "min_bank", "pieces_past_due", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    #outlier detection
    #for i,j in enumerate(names):
    #    plt.figure(figsize=(12,15))
    #    plt.subplot(8,5,i+1)
    #    sns.boxplot(y=j,data=data)

    #Outlier removal
    print("Old Shape: ", data.shape)

    def remove_outliers(data,par):
        z = np.abs(stats.zscore(data[par]))
        a=np.where(z > 3)
        for i in a[0]:
            if i in data.index:
                data.drop(index=i,inplace=True)
            
        #for i in b[0]:
            #if i in data.index:
                #data.drop(index=i,inplace=True)

    for j in ["national_inv",	"in_transit_qty",	"forecast_3_month",	"forecast_6_month"	,"forecast_9_month"	,"sales_1_month", "sales_3_month", "sales_6_month", "sales_9_month", "min_bank", "pieces_past_due", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]: 
        remove_outliers(data,j)
    
    print(data)
    return data

data_preprocess()
