import numpy as np
import matplotlib.pyplot as plt
import time

So = 58
r = 0.1
q = 0.04

def underlying_price(r, q, dt, sgm, So, nbr_sim, T, K):
    start_time = time.time()
    time_axis = np.arange(0, T, dt)
    Maturity = np.ones(shape = (nbr_sim, time_axis.size)) * dt
    Maturity[:,0] = 0
    drift = ((r - q) - (sgm**2) / 2) * Maturity
    diffusion = sgm * np.random.normal(0, np.sqrt(Maturity))
    M = drift + diffusion
    Sint = np.cumsum(M, 1)
    St = So * np.exp(Sint)
    St = np.transpose(St)
    moyenne = np.sum(St[-1, :]) / St.shape[1]
    A = np.array([moyenne - K, 0])
    payoff = np.exp(- r * T) * np.max(A)
    end_time = time.time()
    elapsed_time = end_time - start_time
    fig, ax = plt.subplots()
    ax.text(0.05, 0.92, f'Execution time {elapsed_time} secondes', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})
    ax.text(0.05, 0.80, f'Respectivly average price of the underlying and option:"\n" {moyenne} and {payoff} dollars', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'green', 'alpha': 0.5, 'pad': 10})
    ax.set_title("Monte-Carlo simulation for WTI oil")
    ax.set(xlabel = "time (year)", ylabel = "price (dollar)")
    ax.plot(time_axis, St, '-', linewidth = 0.5)
    plt.show()
    return()

underlying_price(r, q, 0.001, 0.03, So, 100, 0.3, 50)