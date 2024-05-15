from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import pandas as pd

file_formats = {
    "csv": pd.read_csv,
    "xls": pd.read_excel,
    "xlsx": pd.read_excel,
    "xlsm": pd.read_excel,
    "xlsb": pd.read_excel,
}

def load_data(uploaded_file):
    ext = uploaded_file.split(".")[-1].lower()
    if ext in file_formats:
        return file_formats[ext](uploaded_file)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def create_agent(openai_api_key, df):
    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_api_key, streaming=True
    )

    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
    )

    return pandas_df_agent

# def get_response(agent, messages):
#     response = agent.run(messages)
#     if isinstance(response, str):
#         response = response.encode('utf-8', 'replace').decode('utf-8')
#     return response

def get_response(agent, messages):
    parsed_messages = [msg["content"] for msg in messages]
    messages_with_prefix = []
    for i, msg in enumerate(parsed_messages):
        if isinstance(msg, dict):
            # Convert dictionary to string
            msg = str(msg)
        if i % 2 == 0:
            messages_with_prefix.append("based upon the uploaded data " + msg)
        else:
            messages_with_prefix.append("give the output aligned to data " + msg)
    response = agent.run(messages_with_prefix)
    if isinstance(response, str):
        response = response.encode('utf-8', 'replace').decode('utf-8')
    return response
