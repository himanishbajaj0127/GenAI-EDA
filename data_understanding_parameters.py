import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def display_field_descriptions(data):
    st.write('### Field description:')
    fd = data.dtypes.reset_index().rename(columns={'index': 'Field Name', 0: 'Field Type'}).sort_values(
        by='Field Type', ascending=False).reset_index(drop=True)
    st.dataframe(fd, use_container_width=True, hide_index=True)

def display_summary_statistics(data):
    st.write('### Summary Statistics:')
    ss = pd.DataFrame(data.describe(include='all').round(2).fillna(''))
    nc = pd.DataFrame(data.isnull().sum()).rename(columns={0: 'count_null'}).T
    ss = pd.concat([nc, ss]).copy()
    st.dataframe(ss, use_container_width=True)

def display_value_counts(data):
    st.write('### Value Counts of Fields:')
    sub_selected = st.sidebar.radio("*Which field should be investigated?*", data.select_dtypes('object').columns)
    vc = data[sub_selected].value_counts().reset_index().rename(columns={'count': 'Count'}).reset_index(drop=True)
    st.dataframe(vc, use_container_width=True, hide_index=True)

def display_missing_values_analysis(data):
    st.write('### Missing Values Analysis:')
    missing_values = data.isnull().sum()
    missing_percentage = (missing_values / len(data)) * 100
    missing_df = pd.DataFrame({'Missing Values': missing_values, 'Percentage': missing_percentage})
    # Highlighting missing values using background gradient
    missing_df_styled = missing_df.style.background_gradient(cmap='Reds', subset=['Missing Values']).format({'Percentage': "{:.2f}%"})
    st.dataframe(missing_df_styled)

def display_data_distribution(data):
    st.write('### Data Distribution:')
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        fig = px.histogram(data, x=col, title=f'Distribution of {col}', marginal='box')
        st.plotly_chart(fig)

def display_correlation_analysis(data):
    st.write('### Correlation Analysis:')
    # Selecting only numeric columns for correlation calculation
    numeric_data = data.select_dtypes(include=[np.number])
    # Create a pair plot
    pairplot = sns.pairplot(numeric_data)
    st.pyplot(pairplot.fig)

def display_outlier_detection(data):
    st.write('### Outlier Detection:')
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        fig = px.violin(data, y=col, box=True, points="all", title=f'Violin Plot of {col}')
        st.plotly_chart(fig)

def display_data_transformation(data):
    st.write('### Data Transformation:')
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    transformation_type = st.selectbox("Select Transformation Type", ["Log Transformation", "Standardization"])
    if transformation_type == "Log Transformation":
        transformed_data = np.log1p(data[numerical_cols])
    elif transformation_type == "Standardization":
        transformed_data = (data[numerical_cols] - data[numerical_cols].mean()) / data[
            numerical_cols].std()
    st.dataframe(transformed_data)

def display_feature_engineering_suggestions(data):
    st.write('### Feature Engineering Suggestions:')
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    
    if len(numerical_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            col1_selected = st.selectbox("Select the first numerical column", numerical_cols)
        with col2:
            col2_selected = st.selectbox("Select the second numerical column", numerical_cols)

        interaction_feature = data[col1_selected] * data[col2_selected]
        fig = px.scatter(x=data[col1_selected], y=data[col2_selected], color=interaction_feature,
                         title='Interaction Feature Visualization')
        st.plotly_chart(fig)
    else:
        st.write("There are not enough numerical columns to create an interaction feature.")

def display_target_variable_analysis(data):
    st.write('### Target Variable Analysis:')
    if 'target_variable' in data.columns:
        fig = px.histogram(data, x='target_variable', title='Distribution of Target Variable')
        st.plotly_chart(fig)
    else:
        st.write("No 'target_variable' column found in the DataFrame.")

def display_interactive_visualization_tools(data):
    st.write('### Interactive Visualization Tools:')
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    fig = px.scatter_matrix(data[numerical_cols], title='Interactive Pair Plot')
    st.plotly_chart(fig)
