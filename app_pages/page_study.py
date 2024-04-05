import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#from src.data_management import load_house_data
#from src.machine_learning.price_study import regression_per_variable, DisplayCorrAndPPS, CalculateCorrAndPPS



def page_study_body():

    
    # load data
    df = load_house_data()

    # hard copied from study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', '1stFlrSF', 'GarageArea']

    st.write("### House Sale Price Study")
    st.write("Business Requirement 1")
    st.info(
        f"The client is interested to understand the patterns from the"
        f" house attributes, so they can learn the most relevant"
        f"variables that are correlated to  SalePrice."
        f"Visualize the relevant variables against the SalePrice."
    )

    # inspect data
    if st.checkbox("Inspect House Database"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"printed below are the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    # st.write("The correlations and plots interpretation converge.") 

    # st.write("**Top Positive correlated features**")

    # st.write("- Houses with larger garages 'GarageArea' are likely to have a higher Sale Price, indicating that buyers value spacious garages.")

    # - An increase in total basement square footage 'TotalBsmtSF' often leads to an increase in the Sale Price, which indicates that basement area is an important factor in house valuation.

    # - The Sale Price tends to rise with the size of the first floor '1stFlrSF', which shows the significance of main-level living space in the housing market.

    # - The Sale Price tends to be higher for houses with better Overall Quality 'OverallQual', affirming that quality is a crucial determinant of property value.

    # - An increase in above-grade living area 'GrLivArea' leads to a rise in the Sale Price, which reflects the market's valuation of living space.


# **Top Negative correlated features**

# - 'KitchenQual_TA'indicates that the Sale Price of houses with average kitchen quality tends to decrease.

# - The Sale Price is typically lower when the garage is not finished, as shown by 'GarageFinish_Unf'.

# - Houses without any masonry veneer area tend to have a lower Sale Price, indicated by 'MasVnrArea_0.0'.

# - Houses without records of the year the garage was built tend to decrease their Sale Price referred to as 'GarageYrBlt_Missing'.

# - The Sale Price usually decreases on houses without garages,  based on 'GarageFinish_None'.

# **Buyers are willing to pay premiums for more space and higher quality in homes, as these patterns demonstrate the significance of size and quality in valuation.**
    st.write(
        f"* We got a report from ProfileReport which allowed us analyse"
        f"* the quality of the data and helped us understand which paths to follow"
        f"* Pearson and Spearman tests were first run to determine which variables to "
        f" inspect further. \n"
        f"The 2 key variables related to a houses sale price are "
        f"**Overall Quality and Ground Living Area**. "
        f"* A correlation study was then conducted in the notebook to better understand how "
        f"those variables were correlated to SalePrice. \n"
        f"Some of the variables that correlate most with Sale Price and were "
        f"studied further are: **{vars_to_study}** \n\n"
        
    )

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation tests in the notebook and the plots below "
        f"give the following indications: \n"
        f"* The larger the Ground Living Area the higher the SalePrice of a house. \n\n"
        f"* The higher Overall Quality values the higher the SalePrice of a house. \n\n"
        f"  This is also true for houses that are of similar size. \n\n"
        f"* The SalePrice of a house is typically higher for a house with a more recent Year Built. \n\n"
        f"* Houses that have been recently remodeled have a higher correlation with Overall Quality which\n\n"
        f" ends up having an impact in the SalePrice \n\n"
    )

    # Individual plots per variable
    if st.checkbox("Sale Price correlation per Variable"):
        df_eda = df.filter(vars_to_study + ['SalePrice'])
        target_var = 'SalePrice'
        regression_per_variable(df_eda, target_var)

    if st.checkbox("Overall Quality correlation against Year Built and Remodel"):
        quality_to_study = ['YearBuilt', 'YearRemodAdd']
        df_eda = df.filter(quality_to_study + ['OverallQual'])
        target_var = 'OverallQual'
        regression_per_variable(df_eda, target_var)

    if st.checkbox("Houses of Similar Area across Quality against Sale Price"):
        fig, axes = plt.subplots(figsize=(8, 5))
        fig = sns.lmplot(data=df, x="GrLivArea", y="SalePrice", ci=None, hue='OverallQual')
        plt.title(f"Houses of Similar Area across Quality", fontsize=20,y=1.05)
        st.pyplot(fig) 

    if st.checkbox("Heatmaps of all Variables and Correlation"):
            df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
            DisplayCorrAndPPS(df_corr_pearson=df_corr_pearson,
                df_corr_spearman=df_corr_spearman, 
                pps_matrix=pps_matrix,
                CorrThreshold=0.6, PPS_Threshold=0.15,
                figsize=(10,10), font_annot=8)