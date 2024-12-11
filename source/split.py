# METADATA [split.py] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Description: This code script contains the function to split the data into training and testing sets.

    # Developed By: 
        # Name: Mohini T
        # Role: Intern, PreProd Corp
        # Code ownership rights: Mohini T, PreProd Corp
    
    # Version:
        # v1.0 Initial version. [Date: 09-12-2024]
        # v1.1 Updated function to be dynamic. [Date: 10-12-2024]

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Dependencies:
        # Python 3.10.15
        # Libraries:
            # Pandas 2.2.3
            # Scikit-learn 1.5.2

# Importing the necessary libraries
import pandas as pd # For data manipulation
from sklearn.model_selection import train_test_split # For splitting the data

def split_data(data, target_column, test_size):
    """
    This function splits the data into training and testing sets and saves them in the data folder.
    
    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data to split.
    target_column (str): The name of the target column.
    test_size (float): The proportion of the data to include in the test split.
    """
    # Split the data into features and target
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Save the data
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)