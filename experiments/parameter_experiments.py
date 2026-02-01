from src.black_scholes import call_price
from src.greeks import delta_call, gamma, vega

S = 100
K = 100
r = 0.05

T_values = [0.25, 0.5, 1.0, 2.0]
sigma_values = [0.1, 0.2, 0.3]

results = []

for T in T_values:
    for sigma in sigma_values:
        price = call_price(S, K, T, r, sigma)
        delta = delta_call(S, K, T, r, sigma)
        gam = gamma(S, K, T, r, sigma)
        veg = vega(S, K, T, r, sigma)

        results.append(
            {
                "T": T,
                "sigma": sigma,
                "price": price,
                "delta": delta,
                "gamma": gam,
                "vega": veg,
            }
        )

if __name__ == "__main__":
    for row in results:
        print(row)
