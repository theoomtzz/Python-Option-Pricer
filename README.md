# 📈 Quant Pricing Library

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Finance](https://img.shields.io/badge/Finance-Quantitative-orange)

---

## 📝 Description

This project is a **quantitative options pricing and risk management library** developed in Python.  
It centralizes mathematical models and financial instruments within a modular, object-oriented architecture designed for extensibility, validation, and quantitative experimentation.

The current objective is to provide robust tools to:

- **Price European options** using the closed-form Black-Scholes formula.
- **Price European and Exotic options (Asian)** using Monte Carlo simulation.
- **Validate pricing models** by analyzing Monte Carlo convergence against exact analytical solutions.
- **Compute Greeks (sensitivities)** using either analytical differentiation or the *Bump and Value* numerical method.

🚧 **Note:** The *Volatility Surface & Volatility Smile* module is currently under development (Work in Progress).

---

## ✨ Features

### 📊 Instruments

#### Underlying
- Spot price  
- Volatility  
- Continuous dividend yield  

#### European Options
- Payoff dependent on terminal price  

#### Asian Options
- Arithmetic average payoff  
- Path-dependent pricing via Monte Carlo  

---

### ⚙️ Pricing Models (`pricing/`)

#### Black-Scholes (Closed Form)
- Exact analytical solution for European options  
- Continuous dividend support  

#### Monte Carlo Simulation
- Geometric Brownian Motion (GBM) simulation  
- Continuous dividend yield support  
- Path generation for exotic options  
- Convergence validation framework  

---

### 📈 Risk Management / Greeks (`risk/`)

#### Analytical Delta
- Exact computation via Black-Scholes  

#### Bump & Value Delta
- Numerical sensitivity approximation  
- Applicable to any option type  

---

### 🌊 Volatility Module (`volatility/`)

🚧 **Work in Progress**

- Volatility smile generation 
- Volatility surface construction  
- Future integration with calibration and pricing engines  

---

## 🧮 Mathematical Framework

The library is built around:

- Risk-neutral valuation
- Geometric Brownian Motion dynamics
- Continuous dividend modeling
- Analytical Black-Scholes benchmarks
- Monte Carlo convergence validation

---

## 🚀 Installation & Usage

```bash
git clone https://github.com/your-user/quant-pricing-lib.git
cd quant-pricing-lib
pip install -r requirements.txt
python main.py
```

The `main.py` file includes a `run_compare()` function that validates Monte Carlo convergence against analytical Black-Scholes pricing.

---

## 🧠 Project Structure

```
data/          # Data management (cleaning, API, scraping)
instrument/    # Financial instruments
pricing/       # Pricing engines (Black-Scholes, Monte Carlo)
risk/          # Greeks and sensitivities
volatility/    # Volatility surfaces & smiles
main.py        # Demonstration & validation script
requirements.txt
```

---

## 🛣️ Roadmap

- [ ] Extend Greeks (Gamma, Vega, Theta, Rho)
- [ ] Implement implied volatility solver
- [ ] Add volatility surface calibration
- [ ] Introduce variance reduction techniques
---
