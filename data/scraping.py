import yfinance as yf
""" Seulement avec un yahoo fiance voir plus tard 


# On scrap la donnée et en ressort un dictionnaire avec comme clé la matuirté et comme value un df qui donne les info sur l'option
def scrap_option_data(ticker: str):
    dat = yf.Ticker(ticker)
    maturities = dat.options
    option_df_dic = {}
    for maturity in maturities:
        # On récupere que les data qui nous interesse 
        df =  dat.option_chain(maturity).calls.loc[:, ['strike', 'bid', 'ask', 'openInterest']]
        # On trie la donnée afin d'avoir des options liquides et donc qui represente le marché à t
        df_filtre = df[(df['bid'] != 0) & (df['ask'] != 0) & (df['strike'] != 0) & (df['openInterest'] >= 50)]
        # On calcule le prix de l'option
        # No arbitrage 
        df_filtre['price'] = (df_filtre['bid'] + df_filtre['ask']) / 2

        df_filtre['spread'] = (df_filtre['ask'] - df_filtre['bid'])

        df_filtre = df_filtre[df_filtre['spread'] < 0.20]

        print(df_filtre)
        # On range les DF
        if not df_filtre.empty:
            option_df_dic[maturity] = df_filtre

    return option_df_dic


def scrap_asset(ticker : str):
    
    return 


"""