import pandas as pd

def cleaning(df):

    """
    Input : pd.DataFrame
    Output : pd.DataFrame

    Description : Filters the DataFrame to keep only no empty rowf 
                  Convert string into float and date type
    """

    # 
    df = df[['Bid', 'Ask', 'Strike', 'Expiry']].dropna()

    df['Bid'] = df['Bid'].str.replace(",", ".").astype(float)
    df['Ask'] = df['Ask'].str.replace(",", ".").astype(float)
    df['Strike'] = df['Strike'].astype(float)

    df['Expiry'] = pd.to_datetime(df['Expiry'], dayfirst=True)
    
    return df