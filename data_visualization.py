import seaborn as sns
from data_preprocessing import data_preprocess
import matplotlib.pyplot as plt
from feature_engg import feature_engg


def data_visualization():

    data=data_preprocess()
    names=["national_inv","sales_1_month", "sales_9_month", "min_bank", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    for i,j in enumerate(names):
        plt.figure(figsize=(12,15))
        plt.subplot(8,5,i+1)
        sns.boxplot(y=j,data=data)

    return data

data_visualization()
