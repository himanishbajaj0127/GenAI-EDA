import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import file_upload
import data_understanding_parameters as dup
import visualisation_studio as vs

# Setting the web app page name
st.set_page_config(page_title='Exploratory Data Analysis App', page_icon=None, layout="wide")

# Injecting custom CSS for assigning theme to app
custom_css = """
body {
  background-color: #FFFFFF;
}

h1, h2, h3, h4, h5, h6 {
  color: #a1c5bd;
}
"""
st.write('<style>' + custom_css + '</style>', unsafe_allow_html=True)

# Setting markdown
st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis App</h1>", unsafe_allow_html=True)

# File upload section
ft, uploaded_file = file_upload.file_upload_sidebar()

if uploaded_file is not None:
    file_path = uploaded_file

    if ft == 'Excel':
        sh = st.sidebar.selectbox("*Which sheet name in the file should be read?*",
                                  pd.ExcelFile(file_path).sheet_names)
        h = st.sidebar.number_input("*Which row contains the column names?*", 0, 100)
    elif ft == 'csv':
        sh = None
        h = None

    data = file_upload.load_data(file_path, ft, sh, h)

    # Pre-processing datasets
    data.columns = data.columns.astype(str).str.replace('_', ' ')
    data = data.reset_index()
    data.columns = data.columns.str.title()

    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Data Overview", "Data Understanding Parameters", "Visualization Studio"])

    with tab1:
        # Overview of the data
        st.write('### 1. Dataset Preview ')
        try:
            st.dataframe(data, use_container_width=True, hide_index=True)
        except:
            st.info("The file wasn't read properly. Please ensure that the input parameters are correctly defined.")
            st.stop()

        # Horizontal divider
        st.divider()

        # Display data dimensions
        st.write('###### The data has the dimensions :', data.shape)

    with tab2:
        # Displaying data understanding parameters
        st.write('### 2. High-Level Overview ')
        
        selected = st.selectbox("Select a parameter to display",
                                ["Data Dimensions",
                                 "Field Descriptions",
                                 "Summary Statistics",
                                 "Value Counts of Fields",
                                 "Missing Values Analysis",
                                 "Data Distribution",
                                 "Correlation Analysis",
                                 "Outlier Detection",
                                 "Data Transformation",
                                 "Feature Engineering Suggestions",
                                 "Target Variable Analysis",
                                 "Interactive Visualization Tools"])
        
        if selected == 'Field Descriptions':
            dup.display_field_descriptions(data)
        elif selected == 'Summary Statistics':
            dup.display_summary_statistics(data)
        elif selected == 'Value Counts of Fields':
            dup.display_value_counts(data)
        elif selected == 'Missing Values Analysis':
            dup.display_missing_values_analysis(data)
        elif selected == 'Data Distribution':
            dup.display_data_distribution(data)
        elif selected == 'Correlation Analysis':
            dup.display_correlation_analysis(data)
        elif selected == 'Outlier Detection':
            dup.display_outlier_detection(data)
        elif selected == 'Data Transformation':
            dup.display_data_transformation(data)
        elif selected == 'Feature Engineering Suggestions':
            dup.display_feature_engineering_suggestions(data)
        elif selected == 'Target Variable Analysis':
            dup.display_target_variable_analysis(data)
        elif selected == 'Interactive Visualization Tools':
            dup.display_interactive_visualization_tools(data)
        else:
            st.write('###### The data has the dimensions :', data.shape)

    with tab3:
        # Visualization section
        st.write('### Visualization Studio')
        vs.render_visual_insights(data)

    # Horizontal divider
    st.divider()

    # My branding
    st.write("**Created by【H】【B】**")
else:
    st.info("Please upload a file to proceed.")