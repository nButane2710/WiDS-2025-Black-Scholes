import numpy as np


def monte_carlo_call(S, K, T, r, sigma, n_sim=100000):
    Z = np.random.normal(0, 1, n_sim)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0)
    return np.exp(-r * T) * np.mean(payoff)


def monte_carlo_put(S, K, T, r, sigma, n_sim=100000):
    Z = np.random.normal(0, 1, n_sim)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(K - ST, 0)
    return np.exp(-r * T) * np.mean(payoff)


def convergence_study(S, K, T, r, sigma, sims_list):
    results = []
    for n in sims_list:
        price = monte_carlo_call(S, K, T, r, sigma, n)
        results.append((n, price))
    return results


if __name__ == "__main__":
    S, K, T = 100, 100, 1
    r, sigma = 0.05, 0.2

    call_mc = monte_carlo_call(S, K, T, r, sigma)
    put_mc = monte_carlo_put(S, K, T, r, sigma)

    print("MC Call:", call_mc)
    print("MC Put :", put_mc)

    sims = [1_000, 5_000, 10_000, 50_000, 100_000]
    for n, price in convergence_study(S, K, T, r, sigma, sims):
        print(f"Sims: {n}, Call Price: {price}")
