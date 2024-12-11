# METADATA [app.py] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Description: This code script contains the Streamlit web app for generating SweetViz reports.

    # Developed By: 
        # Name: Mohini T
        # Role: Intern, PreProd Corp
        # Code ownership rights: Mohini T, PreProd Corp
    
    # Version:
        # v1.0 Initial version. [Date: 09-12-2024]
        # v1.1 Added the functionality to generate SweetViz reports. [Date: 10-12-2024]
        # v1.2 Fixed comparison by feature report generation. [Date: 11-12-2024]

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Dependencies:
        # Python 3.10.15
        # Libraries:
            # Streamlit 1.40.2
            # Pandas 2.2.3

# Importing the necessary libraries
import streamlit as st # For creating the web app
import pandas as pd # For data manipulation

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
        # Radio button to choose between uploading a file or entering a file path
        dataset_choice = st.radio("Choose an option to upload the data", ["Upload the file", "Enter the path"], horizontal=True)
        dataset_bool = True if dataset_choice == "Upload the file" else False

        # File uploader for CSV files
        data_upload = st.file_uploader("Upload a CSV file",
                                    type="csv",
                                    help="Upload a CSV file to generate a report.",
                                    disabled=not dataset_bool)
        
        # Text input for entering the file path
        data_filepath = st.text_input("Enter the path to the CSV file",
                                help="Enter the complete path to the source data.",
                                disabled=dataset_bool)
        
        if st.button("Ingest", use_container_width=True):
            # Read the uploaded file or the file from the entered path
            if dataset_bool:
                st.session_state.data = pd.read_csv(data_upload)
            else:
                st.session_state.data = pd.read_csv(data_filepath)
            
            # Display success or error message based on data ingestion
            if st.session_state.data is not None:
                st.success("Data ingested successfully!", icon="✅")
            else:
                st.error("Error ingesting data!", icon="❌")

    # Form to display data configuration (number of rows, columns, and first 5 rows)
    with st.form(key="data_config"):
        st.subheader("Data Configuration")
        if st.form_submit_button("Run", use_container_width=True):
            if st.session_state.data is not None:
                st.write(f"Number of rows: {st.session_state.data.shape[0]}")
                st.write(f"Number of columns: {st.session_state.data.shape[1]}")
                st.write(st.session_state.data.head())
            else:
                st.error("No data available to display!", icon="❌")

    # Form to drop the uploaded file and clear the data from session state
    with st.form(key="drop_data"):
        st.subheader("Drop Uploaded File")
        if st.form_submit_button("Drop", use_container_width=True):
            if st.session_state.data is not None:
                st.session_state.data = None
                st.success("Data dropped successfully!", icon="✅")
            else:
                st.error("No file available to drop!", icon="❌")

# Data Preprocessing tab
with tab2:
    st.subheader("Data Preprocessing 🪛")

    # Form to set the target variable
    with st.form(key="Set Target Variable"):
        st.subheader("Set Target Variable")
        if st.session_state.data is not None:
            target_column = st.selectbox("Select the target column", st.session_state.data.columns, index=0)
        else:
            st.error("No data available to select columns from!", icon="❌")
        if st.form_submit_button("Set", use_container_width=True):
            st.session_state.target_column = target_column
            st.success("Target column set successfully!", icon="✅")
    
    # Form to split the data into training and testing sets
    with st.form(key="split_data", border=True):
        st.subheader("Split Data")

        col1, col2 = st.columns(2)

        with col1:
            # Input for training data split percentage
            train_size = st.number_input("Training Data Split %",
                          placeholder="% of training data",
                          help="Enter the percentage of data to be used for training",
                          value=70)
        
        # Calculate and display testing data split percentage
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

# Generate SweetViz Reports tab
with tab3:
    st.subheader("Generate SweetViz Reports 📋")

    # Form to generate full SweetViz report
    with st.form(key="full-report"):
        st.subheader("Full Report")

        # Expander for additional information about the full report
        with st.expander("Learn more about the full SweetViz report", expanded=False):
            st.write("Our app leverages SweetViz to generate an all-encompassing EDA report, providing a detailed overview of dataset statistics, distributions, and relationships. With just a few clicks, you can gain a deep understanding of your data directly in the app.")
        
        if st.form_submit_button("Generate Full Report", use_container_width=True):
            if st.session_state.data is not None:
                generate_full_report(st.session_state.data)
                st.success("Full report generated successfully!", icon="✅")
            else:
                st.error("No data available to generate report!", icon="❌")

    # Form to generate train vs test SweetViz report
    with st.form(key="train-test-report"):
        st.subheader("Train vs Test Report")

        # Expander for additional information about the train vs test report
        with st.expander("Learn more about comparing training and testing datasets", expanded=False):
            st.write("The app utilizes SweetViz to compare training and testing datasets, visually highlighting differences in distributions and feature behavior. This ensures your dataset splits are consistent and ready for machine learning tasks.")
        
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

    # Container to generate comparison by feature report
    with st.container(key="comparison-report", border=True):
        st.subheader("Feature Comparison Report")

        # Expander for additional information about the comparison by feature report
        with st.expander("Learn more about comparing intra-set characteristics", expanded=False):
            st.write("With our app, you can use SweetViz to explore intra-set characteristics by comparing data subsets with exactly 2 unique values based on a selected feature. This helps uncover meaningful group-level insights, such as gender-based trends or other categorical splits.")

        # Dropdown to select the feature for comparison
        feature = st.selectbox("Select the feature to compare",
                                st.session_state.data.columns,
                                help="The selected feature must have only two unique values.",
                                disabled=st.session_state.data is None)
        
        # Display the number of unique values of the selected feature
        st.write(f"Number of unique values of {feature}: {st.session_state.data[feature].nunique()}")

        # Check if the selected feature has exactly two unique values
        if st.session_state.data[feature].nunique() != 2:
            st.warning("Feature must have only two unique values to generate comparison report!")
            disabled = True
        else:
            disabled = False
        
        # Button to generate comparison by feature report
        if st.button("Generate Comparison by Feature Report", use_container_width=True, disabled=disabled):
            generate_comparison_by_feature(st.session_state.data, feature)
            st.success("Comparison report generated successfully!", icon="✅")