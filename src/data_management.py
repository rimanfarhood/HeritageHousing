import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def housing_data():
    df = pd.read_csv("outputs/datasets/cleaned/CleanedHousePricing.csv")
    return df


def inherited_house_data():
    in_df = pd.read_csv("inputs/datasets/raw/house-price/house-price/inherited_houses.csv")
    return in_df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

# code copied from Code Institute's Churnornmeter Project with some adjustments