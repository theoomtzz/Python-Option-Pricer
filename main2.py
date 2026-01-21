import numpy as np
import matplotlib.pyplot as plt
import time

# Class 

class Underlying():
    def __init__(self, ticker, price, dividend, volatility):
        self.ticker = ticker
        self.price = price
        self.dividend = dividend # dividend yield
        self.volatility = volatility 
        self.price_path = None

class Option():
    def __init__(self, category, underlying, maturity, strike):
        self.category = category # call or Put
        self.maturity = maturity
        self.strike = strike
        self.underlying = underlying
        self.price = None

    def payoff(self, paths):
        """
        paths: numpy array de forme (M, N+1) 
        M = nombre de simulations, N = pas de temps
        """
        pass

class EuropeanOption(Option):
        def __init__(self, category, underlying, maturity, strike, type):
            super().__init__(category, underlying, maturity, strike)
            self.type = "european"

        def actucalise_payoff(self, price_paths, r):
            # On isole les prix finaux de la derniere ligne
            St = price_paths[-1, :] 

            if self.category == "call":
                payoff = np.maximum(St - self.strike, 0)

            elif self.category == "put":
                payoff = np.maximum(self.strike - St, 0)

            else:
                raise ValueError(f"category invalide: {self.category} (attendu 'call' ou 'put')")
            
            # Moyenne actualisé des payoff
            return np.exp(- r * self.maturity) * np.mean(payoff)

class AsianOption(Option):
        def __init__(self, category, underlying, maturity, strike, type):
            super().__init__(category, underlying, maturity, strike)
            self.type = "asian"
            
        def actucalise_payoff(self, price_paths, r):
            # On isole les prix finaux de la derniere ligne
            St = price_paths[:, :] 
            
            if self.category == "call":
                payoff = np.maximum(np.mean(St, axis = 0) - self.strike, 0)

            elif self.category == "put":
                payoff = np.maximum(self.strike - np.mean(St, axis = 0), 0)

            else:
                raise ValueError(f"category invalide: {self.category} (attendu 'call' ou 'put')")
            
            # Moyenne actualisé des payoff
            return np.exp(-r * self.maturity) * np.mean(payoff) 

def price_monte_carlo(option, dt, sim_nbr, r):

    # Parameter
    T = option.maturity
    q = option.underlying.dividend
    sgm = option.underlying.volatility
    So = option.underlying.price
    K = option.strike

    # Time axis and matrix
    time_axis = np.arange(0, T, dt)
    Maturity = np.ones(shape = (sim_nbr, time_axis.size)) * dt
    Maturity[:,0] = 0

    # Calcule de St
    drift = ((r - q) - (sgm**2) / 2) * Maturity
    diffusion = sgm * np.random.normal(0, np.sqrt(Maturity))
    Sint = So * np.exp(np.cumsum(drift + diffusion, 1))

    # Transposion pour les futures graphes
    St = np.transpose(Sint)
    return time_axis, St

def drawn(time_axis, St):
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

def main(dt, sim_nbr, r):

    # Initialisation des objets: 
    underlying_1 = Underlying("APPL", price = 50, dividend = 0.05, volatility = 0.25)
    option_1 = EuropeanOption("call", underlying = underlying_1, maturity = 1, strike = 49)
    option_2 = EuropeanOption("put", underlying = underlying_1, maturity = 1, strike = 49)
    option_3 = AsianOption("call", underlying = underlying_1, maturity= 1, strike = 52)

    # Execution de Monte Carlo 
    t_1, price_paths_1 = price_monte_carlo(option_1, dt, sim_nbr, r)
    t_2, price_paths_2 = price_monte_carlo(option_2, dt, sim_nbr, r)
    t_3, price_paths_3 = price_monte_carlo(option_3, dt, sim_nbr, r)

    # Calcul du payoff 
    option_1.price = option_1.actucalise_payoff(price_paths_1, r)
    option_2.price = option_2.actucalise_payoff(price_paths_2, r)
    option_3.price = option_3.actucalise_payoff(price_paths_3, r)

    #Affichage du payoff
    print(option_1.price)
    print(option_2.price)
    print(option_3.price)

    """
    #Affichage des simulations
    time_axis = np.arange(0, 1, dt)
    fig, ax = plt.subplots()
    ax.text(0.05, 0.92, f'Execution time  secondes', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})
    ax.text(0.05, 0.80, f'Respectivly average price of the underlying and option:"\n"  and  dollars', 
        style='italic', 
        transform=ax.transAxes,
        bbox={'facecolor':'green', 'alpha': 0.5, 'pad': 10})
    ax.set_title("Monte-Carlo simulation for WTI oil")
    ax.set(xlabel = "time (year)", ylabel = "price (dollar)")
    ax.plot(time_axis,  price_paths_1, '-', linewidth = 0.5)
    plt.show()"""

main(dt = 0.001, sim_nbr = 1000, r = 0.07)