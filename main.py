import matplotlib.pyplot as plt
import numpy as np
from instrument.instruments import MarketEnvironment, Underlying, EuropeanOption, AsianOption, Option
from pricing.monte_carlo import price_monte_carlo
from pricing.black_scholes import bs_close_form
from risk.grecs import delta_bump, delta_bs
#from data.scraping import scrap_option_data
#from volatility.implied_vol import implied_vol_cal
from data.get_data import get_data
from data.cleaning import cleaning
from data.add_data import add_data
import yfinance as yf

def run_compare():

    # Paramètres
    seed_val = 122
    r_rate = 0.05
    dt_step = 1/252 # 1 jour de trading
    n_sims = 10000

    # Création des underlying
    apple = Underlying("AAPL", 0.80, 10, 0)

    # Création de l'environnement de marché
    env = MarketEnvironment(risk_free_rate = r_rate)
    
    # Création des contrats
    call_eur = EuropeanOption("call", apple, maturity = 1.0, strike = 100)
    put_asian = AsianOption("put", apple, maturity = 1.0, strike = 100)
    
    # MC
    t, paths_eur = price_monte_carlo(call_eur, env, dt_step, n_sims, seed_val)
    _, paths_asian = price_monte_carlo(put_asian, env, dt_step, n_sims, seed_val)
 
    # Pricing
    mc_price_call_eur = call_eur.compute_present_value(paths_eur, env.risk_free_rate)
    mc_price_put_asian = put_asian.compute_present_value(paths_asian, env.risk_free_rate)
    bs_price_call_eur = bs_close_form(call_eur, env)

    # Grecs
    d_bump_call_eur = delta_bump(call_eur, env, dt_step, n_sims, seed_val)
    d_bump_put_asian = delta_bump(put_asian, env, dt_step, n_sims, seed_val)
    d_bs_call_eur = delta_bs(call_eur, env.risk_free_rate)

    # Affichage
    print("\n")
    print(f"----------- Pricing Report for {apple.ticker} -----------")
    print(f"Spot: {apple.price}, Strike: {call_eur.strike}, Vol: {apple.volatility}, T: {call_eur.maturity}")
    print("-" * 47)
    print(f"BS Closed Form (Eur Call) : {bs_price_call_eur:.4f}")
    print(f"MC (Eur Call)             : {mc_price_call_eur:.4f} (Err: {abs(mc_price_call_eur - bs_price_call_eur):.4f})")
    print(f"MC (Asian Put)           : {mc_price_put_asian:.4f}")
    print("-" * 47)
    print(f"Delta bump and value (Eur Call) : {d_bump_call_eur:.4f}")
    print(f"Delta BS (Eur Call)             : {d_bs_call_eur:.4f} (Err: {abs(d_bs_call_eur - d_bump_call_eur):.4f})")
    print(f"Delta bump and value (Asian Put) : {d_bump_put_asian:.4f}")
    print("-" * 47)
    print("\n")

    # Check Visuel
    #fig, ax = plt.subplots()
    #ax.set_title("Monte Carlo Paths - AAPL")
    #ax.set(xlabel = "Time (Years)", ylabel = "Price (dollar)")()
    #ax.plot(t, paths_eur[:, 0:20], '-', linewidth = 0.5)
    #plt.show()

    return

def run_surface():

    r_rate = 0.0475
    market_env = MarketEnvironment(r_rate)
    apple = Underlying("AAPL", 0.1, 242.84, 0)
    path = "/Users/theomettez/Desktop/PostECE/Pricer/data/apple_option_cote.csv"
    t = "6/12/2024" # Today Date 
    
    # Upload data from csv
    df = get_data(path)
    # Data processing
    df = cleaning(df)
    # Add market price and spreand
    df = add_data(df)
    print(df.describe())
    print(df)
    # Récuperation des volaitlité implicite
    
    call_eur = Option('call', apple, np.array(df['Expiry']), np.array(df['Strike']))


    df['bs_price'] = bs_close_form(call_eur, market_env)
   

    #print(df)
    

    # Tracé des smils

    # Creation d'un objet pour utiliser les pricer deja fait  

    return

if __name__ == "__main__":
    
    #run_compare()
    run_surface()





