from sklearn.preprocessing import LabelEncoder
from data_preprocessing import data_preprocess
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def feature_engg():
    data = data_preprocess()
    le=LabelEncoder()
    
    data['potential_issue']=le.fit_transform(data['potential_issue'])
    data['deck_risk']=le.fit_transform(data['deck_risk'])
    data['oe_constraint']=le.fit_transform(data['oe_constraint'])
    data['ppap_risk']=le.fit_transform(data['ppap_risk'])
    data['stop_auto_buy']=le.fit_transform(data['stop_auto_buy'])
    data['rev_stop']=le.fit_transform(data['rev_stop'])
    data['went_on_backorder']=le.fit_transform(data['went_on_backorder'])
    print(data.head())

    X=data.drop(columns="went_on_backorder")
    y=data['went_on_backorder']
    target = le.fit_transform(np.ravel(y))
    
    sm = SMOTE()
    #X_upd, y_upd = sm.fit_resample(X, target.ravel())

    data_new=X #X_upd
    data_new['went_on_backorder']=target.ravel() 
    data_new.to_csv("backorder_prediction.csv")

    return data_new

feature_engg()
