import numpy as np
import matplotlib.pyplot as plt
import time

So = 58
r = 0.1
q = 0.04

# Class --------------------------------------------------------------------------------------------------

# Class parent des underlying 

class Underlying:
    def __init__(self, t: float, T: float, sgm: float):
        self.t = t
        self.T = T
        self.sgm = sgm

        
class MonteCarloEngine:
    def __init__(self):

        pass

# Class parent d'option (moule général)
class Option:

    def __init__(self, K: float, T: float, gender: str): # constructeur de la class Option / self est une convention qui correspond 
        self.K = K # Strike
        self.T = T # Maturity
        self.gender = gender # Call or Putt

# Class enfant d'option (héritée de parents)
class European(Option):

    def  get_european_payoff(self, ST: float):
        if self.gender == "call":
            return(ST - self.K)
        elif self.gender == "put":
            return(self.K - ST)
        else:
            print(" Error: European call or put ? ")

def main():
    O = European(50, 1, "call")
    O = O.get_european_payoff(80)
    print(O)
    return

main()

def underlying_price(r: float, q: float, dt: float, sgm: float, So: float, nbr_sim: int, T: float):
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
underlying_price()