import seaborn as sns
from data_preprocessing import data_preprocess
import matplotlib.pyplot as plt


def data_visualization():

    data=data_preprocess()
    #plt.figure(figsize=(10,8))
    #sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    #plt.show()

    names_cat=["deck_risk","ppap_risk","stop_auto_buy"]
    for i in names_cat:
        plt.subplots(1,1, figsize=(10,8))#plt.figure(figsize=(10,8))
        sns.displot(x=data[i])
        plt.xlabel(i)
        plt.title(i)
    plt.show()
    
    names=["national_inv","sales_1_month", "sales_9_month", "min_bank", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    for i,j in enumerate(names):
        plt.figure(figsize=(10,8))
        #plt.subplot(8,5,i+1)
        sns.boxplot(y=j,data=data)
    plt.show()

    for i in names:
        plt.figure(figsize=(10,8))
        plt.bar(data["went_on_backorder"],data[i])
        plt.xlabel(i)
        plt.title(i)
    plt.show()

    
    return data

data_visualization()
