import numpy as np

# 1. L'objet "de base"
class Underlying:
    def __init__(self, ticker, S0, sigma):
        self.ticker = ticker
        self.S0 = S0        # Prix actuel
        self.sigma = sigma  # Volatilité

# 2. L'objet "Conteneur" (qui contient l'Underlying)
class EuropeanOption:
    def __init__(self, underlying, K, T, kind="call"):
        self.underlying = underlying  # <--- LA CLEF EST ICI
        self.K = K
        self.T = T
        self.kind = kind

# 3. Le Moteur (regarde comme la signature est propre !)
def price_monte_carlo(option, r, n_sim=10000):
    # On va "chercher" les infos en descendant dans les objets
    # C'est ici que tu fais ton "objet.objet.attribut"
    S0 = option.underlying.S0       
    sigma = option.underlying.sigma 
    T = option.T
    K = option.K
    
    # --- Le calcul reste le même ---
    dt = T / 252
    Z = np.random.normal(0, 1, n_sim)
    
    # Formule directe de S_T (solution exacte de l'EDS)
    # S_T = S0 * exp(...)
    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T) * Z
    ST = S0 * np.exp(drift + diffusion)
    
    # Payoff
    if option.kind == "call":
        payoff = np.maximum(ST - K, 0)
    else:
        payoff = np.maximum(K - ST, 0)
        
    return np.exp(-r * T) * np.mean(payoff)

# --- UTILISATION ---

# 1. Je crée l'actif
apple = Underlying("AAPL", S0=120, sigma=0.2)

# 2. Je crée l'option EN LUI DONNANT l'actif
# Mon option "contient" maintenant Apple
mon_call = EuropeanOption(underlying=apple, K=125, T=1) 

# 3. Je price (je n'ai besoin de passer que l'option !)
prix = price_monte_carlo(mon_call, r=0.05)

print(f"Prix du Call sur {mon_call.underlying.ticker} : {prix:.4f}")