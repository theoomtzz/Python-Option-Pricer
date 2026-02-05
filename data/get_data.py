import pandas as pd

def get_data(path: str):

    """
    Input : csv's path
    Output : pd.DataFrame
    
    Description: convert csv to pd.DataFrame
    """

    return pd.read_csv("/Users/theomettez/Desktop/PostECE/Pricer/data/apple_option_cote.csv", sep = ';')
