# Exploratory Data Analysis (EDA) App Documentation

## Introduction

Welcome to the Exploratory Data Analysis (EDA) App! This interactive web-based tool is designed to empower users with the ability to effortlessly explore and analyze datasets. Whether you're a data scientist, analyst, or researcher, this app provides a seamless experience for gaining valuable insights from your data.

## Features

### User-friendly Interface
The app offers a clean and intuitive interface, making it easy for users to navigate and interact with their data.

### Flexible File Upload
Users can upload datasets in either Excel or CSV format, ensuring compatibility with a wide range of data sources.

### Comprehensive Data Understanding
Gain a deep understanding of your data through various analysis options, including:
- **Field Descriptions**: View detailed information about each field in your dataset.
- **Summary Statistics**: Get key summary statistics for numerical fields, helping you understand the distribution and variability of your data.
- **Value Counts of Fields**: Explore the frequency of unique values in categorical fields.
- **Missing Values Analysis**: Identify and analyze missing values in your dataset.
- **Data Distribution**: Visualize the distribution of numerical data through histograms.
- **Correlation Analysis**: Explore the relationships between numerical variables through correlation matrices and pair plots.
- **Outlier Detection**: Detect outliers in your data using violin plots.
- **Data Transformation**: Apply transformations such as log transformation or standardization to numerical data.
- **Feature Engineering Suggestions**: Generate new features or interactions based on existing variables.
- **Target Variable Analysis**: Analyze the distribution of your target variable, if applicable.
- **Interactive Visualization Tools**: Explore your data visually through interactive pair plots and other visualization tools.

### Visualization Studio
Dive deeper into your data with the Visualization Studio, powered by PyGWalker. This feature-rich tool allows for interactive exploration and visualization of your dataset, providing valuable insights at a glance.

### Chatbot Integration
Engage with your data using the DataSense ChatBot. This AI-powered chatbot, integrated with OpenAI's API, allows for conversational data exploration, enhancing the interactivity and usability of the app.

### Customization Options
Customize the app's appearance and behavior to suit your preferences, including theme selection and dataset upload options.

### Documentation and Branding
Access comprehensive documentation to guide you through the app's features and branding information at the end of the app.

## Requirements

To run the EDA App, ensure you have the following prerequisites installed:

- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy
- Plotly
- SciPy
- PyGWalker
- OpenAI
- Tabulate

## Installation and Usage

1. **Install Python 3.x and the required libraries**:
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the app using Streamlit**:
   ```sh
   streamlit run streamlit_app.py
   ```

## Application Walkthrough

### 1. File Upload

- Navigate to the "Data Overview" tab.
- Upload a data file (Excel or CSV).
- Select the appropriate sheet name and header row for Excel files.

### 2. Data Overview

- Preview the dataset.
- View dataset dimensions.

### 3. Data Understanding Parameters

- Select various EDA parameters to analyze the dataset.
- Options include field descriptions, summary statistics, missing values analysis, and more.

### 4. Visualization Studio

- Use the Visualization Studio to create interactive plots and visual insights.

### 5. Chatbot

- Navigate to the "Chatbot" tab.
- Enter your OpenAI API key in the sidebar.
- Interact with the AI-powered chatbot to explore the dataset conversationally.

## Conclusion

The Exploratory Data Analysis App simplifies the process of exploring and analyzing datasets, empowering users to uncover valuable insights and make informed decisions. Whether you're a seasoned data professional or just starting out, this app is your go-to tool for data exploration and discovery.

**Created by【H】【B】**
