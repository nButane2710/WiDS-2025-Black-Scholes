import math
from scipy.stats import norm
from .black_scholes import d1


def delta_call(S, K, T, r, sigma, q=0.0):
    return math.exp(-q * T) * norm.cdf(d1(S, K, T, r, sigma, q))


def delta_put(S, K, T, r, sigma, q=0.0):
    return delta_call(S, K, T, r, sigma, q) - math.exp(-q * T)


def gamma(S, K, T, r, sigma, q=0.0):
    D1 = d1(S, K, T, r, sigma, q)
    return (
        math.exp(-q * T)
        * norm.pdf(D1)
        / (S * sigma * math.sqrt(T))
    )


def vega(S, K, T, r, sigma, q=0.0):
    D1 = d1(S, K, T, r, sigma, q)
    return S * math.exp(-q * T) * norm.pdf(D1) * math.sqrt(T)


if __name__ == "__main__":
    S, K, T = 100, 100, 1
    r, sigma = 0.05, 0.2

    print("Call Delta:", delta_call(S, K, T, r, sigma))
    print("Put Delta :", delta_put(S, K, T, r, sigma))
    print("Gamma     :", gamma(S, K, T, r, sigma))
    print("Vega      :", vega(S, K, T, r, sigma))
