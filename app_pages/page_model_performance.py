import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_management import housing_data, load_pkl_file
from src.machine_learning.model_evaluation import regression_performance, regression_evaluation_plots


def page_model_performance_body():

    # Load sale price pipeline files
    version = 'v1'
    sale_price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_SalePrice/{version}/pipeline.pkl")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predict_SalePrice/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/X_test.csv")
    y_train = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/y_train.csv")
    y_test = pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/y_test.csv")

    st.write("### Model Performance")
    # Display pipeline training summary conclusions
    st.write(
        "Both regressor pipelines did reach above the expected performance"
        " threshold (0.75 R2 score) for the train and test set.\n\n"
        " The regression pipeline without PCA performed better with a higher R2"
        " score and less decrees on the test sets R2 Score\n\n"

        " The data for the pipeline was tuned by taking several steps "
        " to clean and engineer it. The highest performing steps "
        " and hyperparameters on the most critical features "
        " are listed below: ")
    st.write("---")

    # Show pipeline steps
    st.write("* ML Pipeline To Predict Price")
    st.code(sale_price_pipe)
    st.write("---")

    # Show best features
    st.write(
        "The Model Was Trained on These  features"
        "The Most important in descending order"
        )
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)
    st.write("---")

    # evaluate performance on both sets   
    st.write("### Model Performance")
    regression_performance(X_train, y_train, X_test, y_test, sale_price_pipe)

    