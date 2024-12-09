# This code scripts contains a function to split the data into training and testing sets and save them in the data folder

import pandas as pd

def split_data(data, target_column):
    """
    This function splits the data into training and testing sets and saves them in the data folder.
    
    Parameters:
    data (pandas.DataFrame): The DataFrame containing the data to split.
    target_column (str): The name of the target column.
    """
    # Split the data into features and target
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    
    # Split the data into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Save the data
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)