
from pricing.black_scholes import bs_close_form
from pricing.year import year_fraction_from_today
from risk.grecs import vega_bs

import numpy as np



































"""
def implied_vol_cal(option, option_df_dic, market_env):
    

    for  key in option_df_dic:

        option.maturity = year_fraction_from_today(key)
        option.strike = np.array(option_df_dic[key]["strike"])
        market_price = np.array(option_df_dic[key]['price'])
        
        sgm_grid = new_raphsen(market_price, option, option_df_dic, market_env)

        #print(price_grid)

    return 


def new_raphsen(price_grid, option, option_df_dic, market_env, esp = 10**-3):

    r = market_env.risk_free_rate
    option.price = price_grid
    option.underlying.volatility = np.ones(price_grid.shape[0])*0.2
    
    error = 2 * esp

    while error > esp:

        sgm_grid_new = option.underlying.volatility  - (bs_close_form(option, market_env) - price_grid) / vega_bs(option, r)
        print(sgm_grid_new)
        error = np.linalg.norm(sgm_grid_new - option.underlying.volatility)
        option.underlying.volatility  = sgm_grid_new

    return 

"""