# This code script contains a function to ingest CSV file

import pandas as pd

def read_data(file_path):
    """
    This function reads a CSV file and returns a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pandas.DataFrame: The DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)