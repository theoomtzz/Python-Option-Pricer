import numpy as np
import yfinance as yf

class MarketEnvironment:
    def __init__(self, risk_free_rate):
        self.risk_free_rate = risk_free_rate
        
class Underlying:
    def __init__(self, ticker, volatility, price, dividend):
        self.ticker = ticker
        self.price = price
        self.dividend = dividend
        self.volatility = volatility
        
        """ si un jour API 
        # Dividend yield (q)
        try:
            info = yf.Ticker(self.ticker).info
            q = info.get("dividendYield", None)

            if q is None:
                raise ValueError("No dividendYield in Yahoo")

            self.dividend = float(q)

        except Exception as e:
            print(f"[WARN] Dividend not found for {self.ticker}, setting q = 0")
            self.dividend = 0.0

        # Spot price
        try:
            self.price = yf.Ticker(self.ticker).fast_info["lastPrice"]
            
        except Exception:
            print(f"[WARN] Price not found for {self.ticker}, setting S0 = None")
            self.price = None"""
        


    """def __init__(self, ticker, price, dividend, volatility):
        self.ticker = ticker
        self.price = price
        self.dividend = dividend
        self.volatility = volatility"""

class Option:
    def __init__(self, category, underlying, maturity, strike, valuation_time = 0.0):
        self.category = category.lower()
        self.underlying = underlying
        self.maturity = maturity
        self.strike = strike
        self.valuation_time = valuation_time
        self.price = None
        

class EuropeanOption(Option):
    def __init__(self, category, underlying, maturity, strike, valuation_time):
        super().__init__(category, underlying, maturity, strike, valuation_time)
        self.type = "European"

    @property
    def time_to_maturity(self):
        return self.maturity - self.valuation_time

    def compute_present_value(self, price_paths, r):
        # Prix final à maturité (Dernière ligne)
        S_T = price_paths[-1, :] 
        
        if self.category == "call":
            payoff = np.maximum(S_T - self.strike, 0)
        elif self.category == "put":
            payoff = np.maximum(self.strike - S_T, 0)
        else:
                raise ValueError(f"category invalide: {self.category} (Expected 'call' or 'put')")
        
        # Actualisation
        return np.exp(-r * self.maturity) * np.mean(payoff)

class AsianOption(Option):
    def __init__(self, category, underlying, maturity, strike):
        super().__init__(category, underlying, maturity, strike)
        self.type = "Asian"

    def compute_present_value(self, price_paths, r):
        # Moyenne arithmétique de tout le chemin (axis=0 est l'axe temporel ici)
        S_average = np.mean(price_paths, axis=0)
        
        if self.category == "call":
            payoff = np.maximum(S_average - self.strike, 0)
        elif self.category == "put":
            payoff = np.maximum(self.strike - S_average, 0)

         # Actualisation
        return np.exp(-r * self.maturity) * np.mean(payoff)
    
