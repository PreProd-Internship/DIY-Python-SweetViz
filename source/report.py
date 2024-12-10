# This code script will contain three functions:
# 1. generate a full report using sweetviz
# 2. generate a train vs test report using sweetviz
# 3. generate a 'comparison by feature' report for features that only have two categories using sweetviz
# These reports will be returned as HTML files.

# Importing required libraries
import sweetviz as sv
import pandas as pd

def generate_full_report(data):
    """
    This function generates a full report using sweetviz.
    
    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data to generate the report on.
    
    Returns:
    str: The path to the HTML file containing the report.
    """
    report = sv.analyze(data)
    report.show_html()
    return 'SWEETVIZ_REPORT.html'

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
    report.show_html()
    return 'SWEETVIZ_TRAIN_TEST_REPORT.html'

# This function will generate comparison report on intra-set characteristics of the chosen feature
# following this format: my_report = sv.compare_intra(my_dataframe, my_dataframe["Sex"] == "male", ["Male", "Female"])
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
    report.show_html()
    return 'SWEETVIZ_COMPARISON.html'