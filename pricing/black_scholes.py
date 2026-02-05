import numpy as np
from scipy.stats import norm
#from instrument.year import year_fraction_act365

def bs_close_form(option, market_env):
    T = option.maturity
    q = option.underlying.dividend
    sgm = option.underlying.volatility
    So = option.underlying.price
    K = option.strike
    r = market_env.risk_free_rate
    dt = T - 0

    d1 = (np.log(So/K) + (r - q + 0.5 * sgm**2) * dt) / (sgm * np.sqrt(dt))
    d2 = d1 - sgm * np.sqrt(dt)

    if option.category == "call":
        bs_price = So * np.exp(-q * dt) * norm.cdf(d1) - K * np.exp(-r * dt) * norm.cdf(d2)
    elif option.category == "put":
        bs_price = - So * np.exp(-q * dt) * norm.cdf(-d1) + K * np.exp(-r * dt) * norm.cdf(-d2)
    else :
        raise ValueError("category must be call or put")
    
    return bs_price
