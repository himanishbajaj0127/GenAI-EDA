import streamlit as st
import pandas as pd

def file_upload_sidebar():
    st.sidebar.write("****File upload****")
    ft = st.sidebar.selectbox("*What is the file type?*", ["Excel", "csv"])
    uploaded_file = st.sidebar.file_uploader("*Upload file here*")
    return ft, uploaded_file

def load_data(file_path, ft, sh, h):
    if ft == 'Excel':
        try:
            data = pd.read_excel(file_path, header=h, sheet_name=sh, engine='openpyxl')
        except:
            st.info("File is not recognised as an Excel file.")
            sys.exit()
    elif ft == 'csv':
        try:
            data = pd.read_csv(file_path)
        except:
            st.info("File is not recognised as a csv file.")
            sys.exit()
    return data
