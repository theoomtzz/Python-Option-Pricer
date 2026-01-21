import numpy as np
import matplotlib.pyplot as plt
import time


# Class 

class Market_Env():
    def __init__(self, vol, r, q):
        self.vol = vol # volatility
        self.r = r # free risk rate
        self.q = q 
        pass
 
class Underlying():
    def __init__(self, ticker, price, market_env):
        self.ticker = ticker
        self.price = price
        self.price = market_env

class Option():
    def __init__(self, cat, underlying, maturity, strike):
        self.cat = cat # Call, Put
        self.maturity = maturity
        self.strike = strike
        self.underlying = underlying

    def payoff(self, paths):
        """
        paths: numpy array de forme (M, N+1) 
        M = nombre de simulations, N = pas de temps
        """
        pass

class EuropeanOption(Option):
        
        def payoff(self, paths, r):
            if self.cat == "call":
                res = np.exp(r * self.maturity) * max([np.sum(paths[-1, :]) / paths.shape[1] - self.strike,0])
            if self.cat == "put":
                res = np.exp(r * self.maturity) * max([self.strike - np.sum(paths[-1, :]) / paths.shape[1],0]) 
            return res
    

def main(step_time, nbr_sim):
    equities_env = Market_Env(0.03, 0.05, 0.02)
    apple_underlying = Underlying("AAPL", 120, equities_env)
    european_call = EuropeanOption("call", apple_underlying, 1, 125)
    time_axis = np.arange(0, european_call.strike, step_time)
    Maturity = np.ones(shape = (nbr_sim, time_axis.size)) * step_time
    Maturity[:,0] = 0
    drift = (( european_call.underlying. - q) - (sgm**2) / 2) * Maturity
    diffusion = sgm * np.random.normal(0, np.sqrt(Maturity))
    int_european_call_price_paths = drift + diffusion
    int_european_call_price_paths = np.cumsum(int_european_call_price_paths, 1)
    int_european_call_price_paths = apple_underlying.price * np.exp(int_european_call_price_paths)
    european_call_price_paths = np.transpose(St)
    moyenne = np.sum(St[-1, :]) / St.shape[1]
    A = np.array([moyenne - K, 0])
    european_call_price = 
    end_time = time.time()
    return(payoff)