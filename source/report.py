# METADATA [report.py] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Description: This code script contains the functions to generate SweetViz reports.

    # Developed By: 
        # Name: Mohini T
        # Role: Intern, PreProd Corp
        # Code ownership rights: Mohini T, PreProd Corp
    
    # Version:
        # v1.0 Initial version. [Date: 09-12-2024]
        # v1.1 Updated all report generation functions. [Date: 10-12-2024]
        # v1.2 Removed redundant return values. [Date: 11-12-2024]

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Dependencies:
        # Python 3.10.15
        # Libraries:     
            # Python 3.10.15
            # SweetViz 2.3.1
            # Pandas 2.2.3

# Importing required libraries
import sweetviz as sv # For generating reports
import pandas as pd # For data manipulation

def generate_full_report(data):
    """
    This function generates a full report using sweetviz.
    
    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data to generate the report on.
    
    Returns:
    str: The path to the HTML file containing the report.
    """
    report = sv.analyze(data)
    report.show_html('SWEETVIZ_REPORT.html')

def generate_train_test_report(X_train, X_test):
    """
    This function generates a train vs test report using sweetviz.
    
    Parameters:
    X_train (pandas.DataFrame): The DataFrame containing the training features.
    X_test (pandas.DataFrame): The DataFrame containing the testing features.
    
    Returns:
    str: The path to the HTML file containing the report.
    """
    report = sv.compare([X_train, 'Train'], [X_test, 'Test'])
    report.show_html('SWEETVIZ_TRAIN_TEST_REPORT.html')

def generate_comparison_by_feature(data, feature):
    """
    This function generates a 'comparison by feature' report for features that only have two categories using sweetviz.
    
    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data to generate the report on.
    feature (str): The feature to generate the comparison report on.
    
    Returns:
    str: The path to the HTML file containing the report.
    """
    report = sv.compare_intra(data, data[feature] == data[feature].unique()[0], [data[feature].unique()[0], data[feature].unique()[1]])
    report.show_html('SWEETVIZ_COMPARISON.html')