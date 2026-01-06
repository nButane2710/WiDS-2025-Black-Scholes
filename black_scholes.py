import math
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def black_scholes_call(S, K, T, r, sigma):
    """
    European Call Option Price using Black-Scholes Formula
    """
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    return S * norm.cdf(D1) - K * math.exp(-r * T) * norm.cdf(D2)

def black_scholes_put(S, K, T, r, sigma):
    """
    European Put Option Price using Black-Scholes Formula
    """
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)
    return K * math.exp(-r * T) * norm.cdf(-D2) - S * norm.cdf(-D1)
