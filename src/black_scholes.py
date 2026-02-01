import math
from scipy.stats import norm


def d1(S, K, T, r, sigma, q=0.0):
    return (math.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (
        sigma * math.sqrt(T)
    )


def d2(S, K, T, r, sigma, q=0.0):
    return d1(S, K, T, r, sigma, q) - sigma * math.sqrt(T)


def call_price(S, K, T, r, sigma, q=0.0):
    D1 = d1(S, K, T, r, sigma, q)
    D2 = d2(S, K, T, r, sigma, q)

    return (
        S * math.exp(-q * T) * norm.cdf(D1)
        - K * math.exp(-r * T) * norm.cdf(D2)
    )


def put_price(S, K, T, r, sigma, q=0.0):
    D1 = d1(S, K, T, r, sigma, q)
    D2 = d2(S, K, T, r, sigma, q)

    return (
        K * math.exp(-r * T) * norm.cdf(-D2)
        - S * math.exp(-q * T) * norm.cdf(-D1)
    )


def put_call_parity_error(S, K, T, r, sigma, q=0.0):
    call = call_price(S, K, T, r, sigma, q)
    put = put_price(S, K, T, r, sigma, q)

    lhs = call - put
    rhs = S * math.exp(-q * T) - K * math.exp(-r * T)

    return abs(lhs - rhs)


if __name__ == "__main__":
    S, K, T = 100, 100, 1
    r, sigma = 0.05, 0.2

    print("Call:", call_price(S, K, T, r, sigma))
    print("Put :", put_price(S, K, T, r, sigma))
    print("Parity error:", put_call_parity_error(S, K, T, r, sigma))
