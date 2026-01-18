import numpy as np
import matplotlib.pyplot as plt
import time

So = 58
r = 0.1
q = 0.04

def underlying_price(r, q, dt, sgm, So, nbr_sim, T):
    start_time = time.time()
    T = np.arange(0, T, dt)
    Maturity = np.ones(shape = (nbr_sim, T.size)) * dt
    Maturity[:,0] = 0
    drift = ((r - q) - (sgm**2) / 2) * Maturity
    diffusion = sgm * np.random.normal(0, np.sqrt(Maturity))
    M = drift + diffusion
    Sint = np.cumsum(M, 1)
    St = So * np.exp(Sint)
    St = np.transpose(St)
    end_time = time.time()
    elapsed_time = end_time - start_time
    fig, ax = plt.subplots()
    ax.text(0.05, 0.92, f'Execution time {elapsed_time} secondes', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})
    moyenne = float(np.sum(St[-1, :]) / St.shape[1])
    ax.text(0.05, 0.80, f'Average Price: {moyenne} dollars', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'green', 'alpha': 0.5, 'pad': 10})
    ax.set_title("Monte-Carlo simulation for WTI oil")
    ax.set(xlabel = "time (year)", ylabel = "price (dollar)")
    ax.plot(T, St, '-', linewidth = 0.5)
    plt.show()
    return()

underlying_price(r, q, 0.0001, 0.03, So, 1000, 0.3)