import numpy as np

# --- Classes ---

class MarketEnvironment:
    underlyings = []
    def __init__(self, risk_free_rate):
        self.risk_free_rate = risk_free_rate
        
class Underlying:
    def __init__(self, ticker, price, dividend, volatility):
        self.ticker = ticker
        self.price = price
        self.dividend = dividend
        self.volatility = volatility

class Option:
    def __init__(self, category, underlying, maturity, strike):
        self.category = category.lower()
        self.maturity = maturity
        self.strike = strike
        self.underlying = underlying

class EuropeanOption(Option):
    def __init__(self, category, underlying, maturity, strike):
        super().__init__(category, underlying, maturity, strike)
        self.type = "European"

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
