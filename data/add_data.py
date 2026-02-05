
def add_data(df):

    df['Market price'] = (df['Ask'] + df['Bid']) / 2
    df['Spread'] = (df['Ask'] - df['Bid'])

    return(df)