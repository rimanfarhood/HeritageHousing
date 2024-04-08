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
	st.write("### Predict House Sale Price")
	st.info(
		"* 2 - The client is interested to predict the house sale price for their 4 "
		"inherited houses, and any other house in Ames, Iowa. "
		)


	in_df = inherited_house_data()

	house1 = in_df.iloc[[0]]
	house2 = in_df.iloc[[1]]
	house3 = in_df.iloc[[2]]
	house4 = in_df.iloc[[3]]

	features = ['GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

	# predict on live data
	
	price1 = predict_sale_price(house1, features, pipeline)
	price2 = predict_sale_price(house2, features, pipeline)
	price3 = predict_sale_price(house3, features, pipeline)
	price4 = predict_sale_price(house4, features, pipeline)

	

	st.write("---")
	
		
	st.write()
	st.write(f"Summed Value for the inherited houses is: 625 133.3$ ")
		
	st.write()
		
	st.write("---")

	st.write("---")
	st.write("Below you can enter the data of the houses you want an estimated price for. "
			"The default values are set to median values of the data set, in case you are missing any. ")

	X_live = DrawInputsWidgets()

	if st.button('Predict Sale Price'):
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
			label= feature,
			min_value= 0, 
			max_value= 10,
            step = 1       
			)
	X_live[feature] = st_widget

	with col2:
		feature = "GrLivArea"
		st_widget = st.number_input(
			label= feature,
			min_value= 1, 
            step= 10
			)
	X_live[feature] = st_widget

	with col3:
		feature = "TotalBsmtSF"
		st_widget = st.number_input(
			label= feature,
			min_value=1, 
            step= 10
			)
	X_live[feature] = st_widget

	with col4:
		feature = "GarageArea"
		st_widget = st.number_input(
			label= feature,
			min_value= 1, 
            step= 10
			)
	X_live[feature] = st_widget

	with col5:
		feature = "YearBuilt"
		st_widget = st.number_input(
			label= feature, 
			max_value= date.today().year,
            step= 1
			)
	X_live[feature] = st_widget

	return X_live
