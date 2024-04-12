import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 
from feature_engine.encoding import OneHotEncoder

# One hot encoded dataset
def ohe_df():
    # Raw dataset
    df = pd.read_csv("outputs/datasets/HousePricing.csv")

    # Fill missing values to One hot encode
    ohe = df.fillna('Missing', inplace=False) 
    encoder = OneHotEncoder(variables=ohe.columns[ohe.dtypes=='object'].to_list(), drop_last=False)
    df_ohe = encoder.fit_transform(ohe)

    return df_ohe

# Correlation function

def Correlation(df, method, key=False, ascending=True):
    correlation = df.corr(method=method)['SalePrice'].sort_values(key=key, ascending=ascending)[1:]
    
    return correlation


# Correlation plot spearman
def CorrelationPlots(method):
    df_ohe = ohe_df()
    corr = Correlation(df_ohe, method, key=abs, ascending=False)

    fig = plt.figure(figsize=(7,5))
    sns.barplot(x=corr[:20].values, y=corr[:20].index)
    plt.title(f'{method} Correlation with Sale Price')
    plt.xlabel('Correlation Coefficient')
    plt.ylabel('Features')
    plt.tight_layout()
    st.pyplot(fig)
