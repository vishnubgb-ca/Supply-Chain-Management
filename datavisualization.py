import seaborn as sns
from data_preprocessing import data_preprocess
import matplotlib.pyplot as plt


def data_visualization():

    data=data_preprocess()
    #plt.figure(figsize=(10,8))
    #sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    #plt.show()
    
    names=["national_inv","sales_1_month", "sales_9_month", "min_bank", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    for i,j in enumerate(names):
        plt.figure(figsize=(10,8))
        #plt.subplot(8,5,i+1)
        sns.boxplot(y=j,data=data)
        plt.show()

    return data

data_visualization()
