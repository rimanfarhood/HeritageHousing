import streamlit as st
import pandas as pd

from src.data_management import housing_data, load_pkl_file, inherited_house_data
from src.machine_learning.prediction_analysis import predict_sale_price
from datetime import date


def page_prediction_body():

	# load predict sale_price files	
	version = 'v1'
	pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_SalePrice/{version}/pipeline.pkl")
	sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv").columns.to_list())
	st.write("# Prediction House Sale Price")
	st.write("---")
	st.subheader("Business Requirement 2")
	st.write(
		"* The client is interested to predict the house sale price for their 4 "
		"inherited houses, and any other house in Ames, Iowa. "
		)
	
	in_df = inherited_house_data()

	house1 = in_df.iloc[[0]]
	house2 = in_df.iloc[[1]]
	house3 = in_df.iloc[[2]]
	house4 = in_df.iloc[[3]]

	features = [
		'GarageArea', 'GrLivArea', 
		'OverallQual','TotalBsmtSF', 
		'YearBuilt']
	st.write("#### Summed Value for the inherited houses is: **625 133.3$** ")

	st.write("**Sale Price for each Inherited House:**")	
	predict_sale_price(house1, features, pipeline)
	predict_sale_price(house2, features, pipeline)
	predict_sale_price(house3, features, pipeline)
	predict_sale_price(house4, features, pipeline)

	st.write("---")
	st.write("Below you can enter the data of the houses you want an estimated price for.")

	# predict on live data
	X_live = DrawInputsWidgets()

	if st.button('Predict Sale Price'):
		st.write("**The Predicted Sale Price:**")
		predict_sale_price(X_live, sale_price_features, pipeline)


def DrawInputsWidgets():

	# load dataset
	df = housing_data()

    # we create input widgets for 5 features 	
	col1, col2 = st.columns(2)
	col3, col4, col5 = st.columns(3)

	# We are using these features to feed the ML pipeline
		
	# create an empty DataFrame, which will be the live data
	X_live = pd.DataFrame([], index=[0]) 
	
	# from here on we draw the widget based on the variable type (numerical or categorical)
	# and set initial values

	with col1:
		feature = "OverallQual"
		st_widget = st.number_input(
			label= 'Overall Quality: Rates the overall material and finish of the house: 1 - 10',
			min_value= 1, 
			max_value= 10,
            step = 1       
			)
	X_live[feature] = st_widget

	with col2:
		feature = "GrLivArea"
		st_widget = st.number_input(
			label= 'Above grade (ground) living area square feet: 334 - 5642',
			min_value= 334,
			max_value= 5642, 
            step= 10
			)
	X_live[feature] = st_widget

	with col3:
		feature = "TotalBsmtSF"
		st_widget = st.number_input(
			label= 'Total square feet of basement area: 0 - 6110',
			min_value= 0,
			max_value= 6110, 
            step= 10
			)
	X_live[feature] = st_widget

	with col4:
		feature = "GarageArea"
		st_widget = st.number_input(
			label= "Garage Area: Size of garage in square feet: 0 - 1418",
			min_value= 0,
			max_value= 1418, 
            step= 10
			)
	X_live[feature] = st_widget

	with col5:
		feature = "YearBuilt"
		st_widget = st.number_input(
			label= "Year Built: Original construction date: 1872-2010", 
			min_value= 1872,
			max_value= 2010,
            step= 1
			)
	X_live[feature] = st_widget

	return X_live
