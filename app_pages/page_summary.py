import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **SalePrice** is the target variable.\n"
        f"* The dataset contains housing profile records for houses built between 1872 and 2010 in Ames, Iowa.\n"
        f"The dataset have various abbreviated terms used to describe their features.\n"
        f"To view the dataset with all the information,"
        f"click **[Link To Dataset](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**.\n\n"
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/rimanfarhood/HeritageHousing/blob/main/README.md).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how house attributes\n"
        f"correlate with sale prices. Therefore, the client expects data\n"
        f"visualizations of the correlated variables against the sale price \n"
        f"* 2 - Deliver an ML model with the capability of predicting the\n"
        f"sale price of the four inherited houses and any house in Ames,"
        f"Iowa with at least 75% accuracy."
        )

        