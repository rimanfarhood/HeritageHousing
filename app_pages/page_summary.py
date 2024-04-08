import streamlit as st


def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.write(
        "**Project Terms & Jargon**\n\n"
        "- **SalePrice** is the target variable.\n\n"
        "The dataset contains housing profile records for houses built "
        "between 1872 and 2010 in Ames, Iowa.\n\n"
        "The dataset have various abbreviated terms used to describe their"
        "features.\n\n"
        "To view the dataset with all the information, "
        "Click -->  **[Link To Dataset]"
        "(https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)"
        "**."
        )
    
    st.write("---")

    # copied from README file - "Business Requirements" section
    st.subheader("Business requirements")
    st.write(
        "**Requirement 1:**\n\n"
        " - The client is interested in discovering how house attributes"
        " correlate with sale prices. Therefore, the client expects data "
        " visualizations of the correlated variables against the sale price\n\n"
        "- The client is interested in predicting the house sale prices "
        "from her 4 inherited houses, and any other house in Ames, Iowa.\n\n"
        )
    st.write(
        "**Requirement 2:**\n\n"
        " - Deliver an ML model with the capability of predicting the\n"
        "sale price of the four inherited houses and any house in Ames,"
        "Iowa with at least 75% accuracy."
        )
    st.write("---")

    # Link to README file, for users to access the full project documentation
    st.write(
        "* For additional information, please visit and **read** the "
        "[Project README file]"
        "(https://github.com/rimanfarhood/HeritageHousePrediction/blob/main/"
        "README.md)."
        )
    
