import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_study import page_study_body
from app_pages.page_prediction import page_prediction_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_model_performance import page_model_performance_body

app = MultiPage(app_name= "Heritage Housing") # Create an instance of the app 

# Add your app pages here using .add_page()
app.app_page("Project Summary", page_summary_body)
app.app_page("House Sale Price Study", page_study_body)
app.app_page("Predict House Value", page_prediction_body)
app.app_page("Project Hypothesis and Validation", page_hypothesis_body)
app.app_page("ML: Predict House Value", page_model_performance_body)

app.run() # Run the  app

