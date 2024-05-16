import streamlit as st
import pandas as pd
import file_upload
import data_understanding_parameters as dup
import visualisation_studio as vs
import chatbot  # Import the chatbot module

def set_page_config():
    st.set_page_config(page_title='DataSense AI', page_icon=None, layout="wide")

def inject_custom_css():
    custom_css = """
    body {
      background-color: #FFFFFF;
    }
    """
    st.write('<style>' + custom_css + '</style>', unsafe_allow_html=True)

def display_header():
    st.markdown("<h1 style='text-align: center;'>DataSense AI</h1>", unsafe_allow_html=True)

def handle_file_upload():
    ft, uploaded_file = file_upload.file_upload_sidebar()
    return ft, uploaded_file

def read_data(file_path, file_type):
    if file_type == 'Excel':
        sheet_name = st.sidebar.selectbox("Which sheet name in the file should be read?", pd.ExcelFile(file_path).sheet_names)
        header_row = st.sidebar.number_input("Which row contains the column names?", 0, 100)
    else:
        sheet_name = None
        header_row = None

    data = file_upload.load_data(file_path, file_type, sheet_name, header_row)
    data.columns = data.columns.astype(str).str.replace('_', ' ')
    data = data.reset_index(drop=True)
    data.columns = data.columns.str.title()
    
    return data

def display_data_overview(data):
    st.write('### 1. Dataset Preview')
    try:
        st.dataframe(data, use_container_width=True, hide_index=True)
    except Exception as e:
        st.info("The file wasn't read properly. Please ensure that the input parameters are correctly defined.")
        st.stop()

    st.divider()
    st.write('###### The data has the dimensions:', data.shape)

def display_data_understanding(data):
    st.write('### 2. EDA Parameters')
    
    selected = st.selectbox("Select a parameter to display", [
        "Data Dimensions",
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
        "Interactive Visualization Tools"
    ])
    
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

def display_visualization_studio(data):
    st.write('### 3. Visualization Studio')
    vs.render_visual_insights(data)

def chat_interface(df, openai_api_key):
    st.write("### 4. DataSense ChatBot 🌏")

    if df is None:
        st.warning(
            "Please upload the file in the Data Overview tab, otherwise you won't be able to talk with the AI DataFrame ChatBot!"
        )
        return

    if not openai_api_key:
        st.warning("Please add your OpenAI API key in the sidebar to continue the GPT-3.5 Turbo conversation.")
        return

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Chat history display
    st.subheader("Chat History")
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f"<font color='#4682B4'>🔵User: {msg['content']}</font>", unsafe_allow_html=True)
        else:
            st.markdown(f"<font color='#FFFFFF'>⚪DataSense AI: {msg['content']}</font>", unsafe_allow_html=True)

    # User input
    user_input = st.text_input("Type your message here:", key="user_input")
    if st.button("Send"):
        if user_input.strip() != "":
            st.session_state["messages"].append({"role": "user", "content": user_input.strip()})
            agent = chatbot.create_agent(openai_api_key, df)
            response = chatbot.get_response(agent, st.session_state["messages"])
            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.markdown(f"<font color='#FFFFFF'>⚪ DataSense AI: {response}</font>", unsafe_allow_html=True)

def main():
    set_page_config()
    inject_custom_css()
    display_header()
    
    file_type, uploaded_file = handle_file_upload()
    
    if uploaded_file is not None:
        with st.spinner('Loading data...'):
            data = read_data(uploaded_file, file_type)

        openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
        
        tab1, tab2, tab3, tab4 = st.tabs(["Data Overview", "Data Understanding Parameters", "Visualization Studio", "Chatbot"])

        with tab1:
            display_data_overview(data)
        
        with tab2:
            display_data_understanding(data)
        
        with tab3:
            display_visualization_studio(data)
        
        with tab4:
            chat_interface(data, openai_api_key)

        st.divider()
        st.write("**Created by【H】【B】**")

    else:
        st.info("Please upload a file to proceed.")

if __name__ == "__main__":
    main()