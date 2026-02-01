from .black_scholes import call_price


def implied_volatility_call(market_price, S, K, T, r, q=0.0, tol=1e-6):
    low = 1e-6
    high = 3.0

    for _ in range(100):
        mid = 0.5 * (low + high)
        price = call_price(S, K, T, r, mid, q)

        if abs(price - market_price) < tol:
            return mid

        if price > market_price:
            high = mid
        else:
            low = mid

    return mid


if __name__ == "__main__":
    S, K, T = 100, 100, 1
    r = 0.05
    true_sigma = 0.2

    market_price = call_price(S, K, T, r, true_sigma)
    iv = implied_volatility_call(market_price, S, K, T, r)

    print("Market Call Price:", market_price)
    print("Implied Volatility:", iv)
