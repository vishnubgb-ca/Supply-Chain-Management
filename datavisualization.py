from data_preprocessing import data_preprocess
import pandas as pd
import plotly.express as px
from IPython.display import Image

def data_visualization():

    data=data_preprocess()
    #plt.figure(figsize=(10,8))
    #sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    #plt.show()

    names_cat=["deck_risk","ppap_risk","stop_auto_buy"]
    for i in names_cat:
        list = []
        list.append(i)
        df = data.groupby(by=list).size().reset_index(name="counts")
        fig=px.bar(data_frame=df, x=i, y="counts",color=i)
        fig.update_layout(plot_bgcolor = "black")
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        #img_bytes = fig.to_image(format="png")
        #f2 = go.FigureWidget(fig)
        fig.show()
        # img_bytes = fig.to_image(format="png")
        # Image(img_bytes)
    
    names=["national_inv","sales_1_month", "sales_9_month", "min_bank", "perf_6_month_avg","perf_12_month_avg", "local_bo_qty"]

    for j in names:
        fig = px.box(data, y=j)
        fig.update_layout(plot_bgcolor = "black")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.show()

    #for i in names:
    #    plt.figure(figsize=(5,5))
    #    plt.bar(data["went_on_backorder"],data[i])
    #    plt.ylabel(i)
    #    plt.xlabel("went_on_backorder")
    #    plt.title(i)
    #plt.show()

    
    return data

data_visualization()
