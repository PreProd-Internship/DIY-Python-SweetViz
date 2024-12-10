# This code script contains the web app using Streamlit to interact with the functions in the other scripts.

import streamlit as st
import pandas as pd

# Importing the functions from the other scripts
from split import split_data
from report import (generate_full_report,
                    generate_train_test_report,
                    generate_comparison_by_feature)

# Initialize session state for data if it doesn't exist
if 'data' not in st.session_state:
    st.session_state.data = None

# Setting the page configuration for the web app
st.set_page_config(page_title="SweetViz", page_icon=":bar_chart:", layout="centered")

# Adding a heading to the web app
st.markdown("<h1 style='text-align: center; color: white;'>Exploratory Data Analysis using Python's SweetViz 📊</h1>", unsafe_allow_html=True)
st.divider()

# Creating tabs for the web app
tab1, tab2, tab3 = st.tabs(["Data Ingestion", "Data Preprocessing", "Generate SweetViz Reports"])

# Data Ingestion tab
with tab1:
    st.subheader("Data Ingestion 📂")

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
        
        if st.button("Ingest", use_container_width=True):
            # Upon clicking this button, if the file is uploaded it will be read by panda's pd.read_csv function,
            # or if the path is entered, the file will be read by the read_data function in the read.py file.
            if dataset_bool:
                st.session_state.data = pd.read_csv(data_upload)
            else:
                st.session_state.data = pd.read_csv(data_filepath)
            
            if st.session_state.data is not None:
                st.success("Data ingested successfully!", icon="✅")
            else:
                st.error("Error ingesting data!", icon="❌")

    # This form will display the data configuration, i.e., upon pressing the "Run" button, no. of rows and columns will be displayed along with the first 5 rows of the data.
    with st.form(key="data_config"):
        st.subheader("Data Configuration")
        if st.form_submit_button("Run", use_container_width=True):
            if st.session_state.data is not None:
                st.write(f"Number of rows: {st.session_state.data.shape[0]}")
                st.write(f"Number of columns: {st.session_state.data.shape[1]}")
                st.write(st.session_state.data.head())
            else:
                st.error("No data available to display!", icon="❌")

    # This form will drop the uploaded file(s) and clear the data from the session state upon the click of "Drop".
    with st.form(key="drop_data"):
        st.subheader("Drop Uploaded File")
        if st.form_submit_button("Drop", use_container_width=True):
            if st.session_state.data is not None:
                st.session_state.data = None
                st.success("Data dropped successfully!", icon="✅")
            else:
                st.error("No file available to drop!", icon="❌")

with tab2:
    st.subheader("Data Preprocessing 🪛")

    with st.form(key="Set Target Variable"):
        st.subheader("Set Target Variable")
        if st.session_state.data is not None:
            target_column = st.selectbox("Select the target column", st.session_state.data.columns, index=0)
        else:
            st.error("No data available to select columns from!", icon="❌")
        if st.form_submit_button("Set", use_container_width=True):
            st.session_state.target_column = target_column
            st.success("Target column set successfully!", icon="✅")
    
    with st.form(key="split_data", border=True):
        st.subheader("Split Data")

        col1, col2 = st.columns(2)

        with col1:
            train_size = st.number_input("Training Data Split %",
                          placeholder="% of training data",
                          help="Enter the percentage of data to be used for training",
                          value=70)
        
        # This is for visual appeal
        test_size = 100 - train_size
        with col2:
            n = st.number_input("Testing Data Split %",
                          placeholder="% of testing data",
                          help="See the percentage of data to be used for testing",
                          value=test_size, disabled=True)
        
        if st.form_submit_button("Split", use_container_width=True):
            if st.session_state.data is not None:
                split_data(st.session_state.data, st.session_state.target_column, test_size=n/100)
                st.success("Data split successfully!", icon="✅")
            else:
                st.error("No data available to split!", icon="❌")

with tab3:
    st.subheader("Generate SweetViz Reports 📋")

    with st.form(key="full-report"):
        st.subheader("Full Report")

        # Expander for theory
        with st.expander("Learn more about the full SweetViz report", expanded=False):
            st.write("Lorem ipsum dolor sit amet")
        
        if st.form_submit_button("Generate Full Report", use_container_width=True):
            if st.session_state.data is not None:
                generate_full_report(st.session_state.data)
                st.success("Full report generated successfully!", icon="✅")
            else:
                st.error("No data available to generate report!", icon="❌")

    with st.form(key="train-test-report"):
        st.subheader("Train vs Test Report")

        # Expander for theory
        with st.expander("Learn more about comparing training and testing datasets", expanded=False):
            st.write("Lorem ipsum dolor sit amet")
        
        if st.form_submit_button("Generate Train vs Test Report", use_container_width=True):
            if st.session_state.data is not None:
                X_train = pd.read_csv('data/X_train.csv')
                X_test = pd.read_csv('data/X_test.csv')
                y_train = pd.read_csv('data/y_train.csv')
                y_test = pd.read_csv('data/y_test.csv')
                generate_train_test_report(X_train, X_test)
                st.success("Train vs Test report generated successfully!", icon="✅")
            else:
                st.error("No data available to generate report!", icon="❌")
'''
    with st.form(key="comparison-report"):
        st.subheader("Comparison by Feature Report")

        # Expander for theory
        with st.expander("Learn more about comparing intra-set characteristics", expanded=False):
            st.write("Lorem ipsum dolor sit amet")

        # The user will now have the chance to pick the feature to compare using the dropdown menu. In the backend, this
        # will be passed to the generate_comparison_by_feature function. There should be a warning if the selected feature has more than two categories,
        # as the function is designed to compare features with exactly two categories.
        if st.session_state.data is not None:
            feature = st.selectbox("Select the feature to compare",
                                    st.session_state.data.columns,
                                    help="The selected feature must have only two unique values.")
            st.write(f"Selected feature: {feature}")
            # The app will show how many unique values the feature has. If the feature has more than two unique values, a warning will be displayed and the button will be disabled.
            # However, if the feature has only two unique values, the function generate_comparison_by_feature will be called and the button will be enabled.
            st.write(f"Number of unique values of {feature}: {st.session_state.data[feature].nunique()}")
            if st.session_state.data[feature].nunique() == 2:
                generate_report = st.form_submit_button("Generate Comparison by Feature Report", use_container_width=True)
                if generate_report:
                    generate_comparison_by_feature(st.session_state.data, feature)
                    st.success("Comparison report generated successfully!", icon="✅")
            else:
                st.warning("Feature must have only two unique values to generate comparison report!")
        else:
            st.error("No data available to generate report!", icon="❌")
'''
        