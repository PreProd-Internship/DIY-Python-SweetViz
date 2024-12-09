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

def generate_train_test_report(X_train, X_test, y_train, y_test):
    """
    This function generates a train vs test report using sweetviz.
    
    Parameters:
    X_train (pandas.DataFrame): The DataFrame containing the training features.
    X_test (pandas.DataFrame): The DataFrame containing the testing features.
    y_train (pandas.Series): The Series containing the training target.
    y_test (pandas.Series): The Series containing the testing target.
    
    Returns:
    str: The path to the HTML file containing the report.
    """
    report = sv.compare([X_train, 'Train'], [X_test, 'Test'], y_train, y_test)
    report.show_html()
    return 'SWEETVIZ_TRAIN_TEST_REPORT.html'

def generate_comparison(data):
    """
    This function generates a 'comparison by feature' report for features that only have two values using sweetviz.
    
    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data to generate the report on.
    
    Returns:
    str: The path to the HTML file containing the report.
    """
    report = sv.compare_intra(data, data.columns, 'target_column')
    report.show_html()
    return 'SWEETVIZ_COMPARISON_BY_FEATURE_REPORT.html'