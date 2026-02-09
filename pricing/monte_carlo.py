import numpy as np

def price_monte_carlo(option, market_env, dt, sim_nbr, seed_val):

    """
    Input : 
        Option object with scalar and without array or df

    Output : 
        Two Arrays : time_path and price_paths 
    """
    
    # Unpacking
    r = market_env.risk_free_rate
    T = option.maturity
    t = option.valuation_time
    q = option.underlying.dividend
    sgm = option.underlying.volatility
    So = option.underlying.price
    np.random.seed(seed_val)
    tau = option.time_to_maturity
    # Time axis and matrix
    """
    N = int(T / dt)
    time_axis = np.linspace(0, T, N + 1)
    dt = T / N # On force le dt à s'adapter
    """
    N = int(tau / dt)
    time_axis = np.linspace(t, T, N + 1)
    dt = tau / N

    Maturity = np.ones(shape = (sim_nbr, time_axis.size)) * dt
    Maturity[:,0] = 0
    
    # Calcule de St
    drift = ((r - q) - (sgm**2) / 2) * Maturity
    diffusion = sgm * np.random.normal(0, np.sqrt(Maturity))
    S_paths = So * np.exp(np.cumsum(drift + diffusion, 1))
    S_paths = np.transpose(S_paths)
    
    return time_axis, S_paths