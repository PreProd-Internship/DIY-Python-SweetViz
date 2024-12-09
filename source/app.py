# This code script contains the web app using Streamlit to interact with the functions in the other scripts.

import streamlit as st
import pandas as pd

# Importing the functions from the other scripts
from split import split_data
from report import (generate_full_report,
                    generate_train_test_report,
                    generate_comparison)

# Initialize session state for data if it doesn't exist
if 'data' not in st.session_state:
    st.session_state.data = None

# Setting the page configuration for the web app
st.set_page_config(page_title="SweetViz", page_icon=":bar_chart:", layout="centered")

# Adding a heading to the web app
st.markdown("<h1 style='text-align: center; color: white;'>Exploratory Data Analysis using SweetViz</h1>", unsafe_allow_html=True)
st.divider()

# Creating tabs for the web app
tab1, tab2, tab3 = st.tabs(["Data Ingestion", "Data Preprocessing", "Generate Reports"])

# Data Ingestion tab
with tab1:
    st.subheader("Data Ingestion")

    with st.container(border=True):
        dataset_choice = st.radio("Choose an option to upload the data", ["Upload the file", "Enter the path"], horizontal=True)
        dataset_bool = True if dataset_choice == "Upload the file" else False

        data_upload = st.file_uploader("Upload a CSV file",
                                    type="csv",
                                    help="Upload a CSV file to generate a report.",
                                    disabled=not dataset_bool)
        
        data_filepath = st.text_input("Enter the path to the CSV file",
                                help="Enter the complete path to the source data.",
                                disabled=dataset_bool)
        
        if st.button("Ingest"):
            # Upon clicking this button, if the file is uploaded it will be read by panda's pd.read_csv function,
            # or if the path is entered, the file will be read by the read_data function in the read.py file.
            if dataset_bool:
                st.session_state.data = pd.read_csv(data_upload)
            else:
                st.session_state.data = pd.read_csv(data_filepath)

            st.write(st.session_state.data)
            
            if st.session_state.data is not None:
                st.success("Data ingested successfully!", icon="✅")
            else:
                st.error("Error ingesting data!", icon="❌")

    # This form will display the data configuration, i.e., upon pressing the "Run" button, no. of rows and columns will be displayed along with the first 5 rows of the data.
    with st.form(key="data_config"):
        st.subheader("Data Configuration")
        if st.form_submit_button("Run"):
            if st.session_state.data is not None:
                st.write(f"Number of rows: {st.session_state.data.shape[0]}")
                st.write(f"Number of columns: {st.session_state.data.shape[1]}")
                st.write(st.session_state.data.head())
            else:
                st.error("No data available to display!", icon="❌")

# This form will drop the uploaded file(s) and clear the data from the session state upon the click of "Drop".
with st.form(key="drop_data"):
    st.subheader("Drop Uploaded File")
    if st.form_submit_button("Drop"):
        if st.session_state.data is not None:
            st.session_state.data = None
            st.success("Data dropped successfully!", icon="✅")
        else:
            st.error("No file available to drop!", icon="❌")

"""
with tab2:
    st.subheader("Data Preprocessing")

    with st.form(key="Set Target Variable"):
        st.subheader("Set Target Variable")
        target_column = st.selectbox("Select the target column", st.session_state.data.columns, index=0)
        if st.form_submit_button("Set"):
            st.session_state.target_column = target_column
            st.success("Target column set successfully!", icon="✅")
    
    # This form will split the data using the split_data function in the split.py file, and will let the end user pick the split.
    with st.form(key="split_data"):
        st.subheader("Split Data")
        if st.form_submit_button("Split"):
            if st.session_state.data is not None:
                split_data(st.session_state.data, st.session_state.target_column)
                st.success("Data split successfully!", icon="✅")
            else:
                st.error("No data available to split!", icon="❌")
"""