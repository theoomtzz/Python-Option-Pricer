import numpy as np
from scipy.stats import norm
from pricing.monte_carlo import price_monte_carlo

def vega_bump(option, market_env, dt_step, n_sims, seed_val):

        r = market_env.risk_free_rate
        eps = 0.1  # petit choc sur le spot
        original_option_vol = option.underlying.volatility

        # Prix spot + eps 
        option.underlying.volatility += eps
        np.random.seed(seed_val)
        _, paths_up = price_monte_carlo(option, market_env, dt_step, n_sims, seed_val)
        price_up = option.compute_present_value(paths_up, r)

        option.underlying.price = original_option_vol

        # Prix spot - eps
        option.underlying.volatility -= eps
        np.random.seed(seed_val)
        _, paths_down = price_monte_carlo(option, market_env, dt_step, n_sims, seed_val)
        price_down = option.compute_present_value(paths_down, r)

        option.underlying.volatility = original_option_vol

        # Vega
        vega = (price_up - price_down) / (2*eps)

        return vega

def vega_bs(option, r):

    T = option.maturity
    q = option.underlying.dividend 
    sgm = option.underlying.volatility
    So = option.underlying.price
    K = option.strike

    d1 = (np.log(So/K) + (r - q + 0.5 * sgm**2) * T) / (sgm * np.sqrt(T))
    vega = So * np.exp(-q * T) * np.sqrt(T - 0) * norm.pdf(d1)

    return vega

def delta_bump(option, market_env, dt_step, n_sims, seed_val):

        r = market_env.risk_free_rate
        eps = 0.1  # petit choc sur le spot
        original_price_option = option.underlying.price

        # Prix spot + eps 
        option.underlying.price += eps
        np.random.seed(seed_val)
        _, paths_up = price_monte_carlo(option, market_env, dt_step, n_sims, seed_val)
        price_up = option.compute_present_value(paths_up, r)

        option.underlying.price = original_price_option

        # Prix spot - eps
        option.underlying.price -= eps
        np.random.seed(seed_val)
        _, paths_down = price_monte_carlo(option, market_env, dt_step, n_sims, seed_val)
        price_down = option.compute_present_value(paths_down, r)

        option.underlying.price = original_price_option

        # Delta
        delta = (price_up - price_down) / (2*eps)

        return delta

def delta_bs(option, r):

    T = option.maturity
    q = option.underlying.dividend 
    sgm = option.underlying.volatility
    So = option.underlying.price
    K = option.strike

    d1 = (np.log(So/K) + (r - q + 0.5 * sgm**2) * T) / (sgm * np.sqrt(T))
    delta = np.exp(-q * T) * norm.cdf(d1)
        
    if option.category == "put":
        delta = np.exp(-q * T) * (norm.cdf(d1) - 1)

    return delta
