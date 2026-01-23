import numpy as np
from scipy.stats import norm

# --- Engine ---

def price_monte_carlo(option, market_env, dt, sim_nbr, seed_val):
    # Unpacking
    r = market_env.risk_free_rate
    T = option.maturity
    q = option.underlying.dividend
    sgm = option.underlying.volatility
    So = option.underlying.price
    np.random.seed(seed_val)
    
    # Time axis and matrix
    N = int(T / dt)
    time_axis = np.linspace(0, T, N + 1)
    dt = T / N # On force le dt à s'adapter
    Maturity = np.ones(shape = (sim_nbr, time_axis.size)) * dt
    Maturity[:,0] = 0
    
    # Calcule de St
    drift = ((r - q) - (sgm**2) / 2) * Maturity
    diffusion = sgm * np.random.normal(0, np.sqrt(Maturity))
    S_paths = So * np.exp(np.cumsum(drift + diffusion, 1))
    S_paths = np.transpose(S_paths)
    
    return time_axis, S_paths

def bs_close_form(option, market_env):
    T = option.maturity
    q = option.underlying.dividend
    sgm = option.underlying.volatility
    So = option.underlying.price
    K = option.strike
    r = market_env.risk_free_rate

    d1 = (np.log(So/K) + (r - q + 0.5 * sgm**2) * T) / (sgm * np.sqrt(T))
    d2 = d1 - sgm * np.sqrt(T)

    if option.category == "call":
        price = So * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option.category == "put":
        price = - So * np.exp(-q * T) * norm.cdf(-d1) + K * np.exp(-r * T) * norm.cdf(-d2)
    else :
        raise ValueError("category must be call or put")
    
    return price

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

def delta_BS(option, r):

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
