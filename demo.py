from black_scholes import black_scholes_call, black_scholes_put
from greeks import delta_call, gamma, vega

S = 100     # Stock price
K = 100     # Strike price
T = 1       # Time to maturity (1 year)
r = 0.05    # Risk-free rate
sigma = 0.2 # Volatility

call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)

print("Call Price:", call_price)
print("Put Price:", put_price)
print("Call Delta:", delta_call(S, K, T, r, sigma))
print("Gamma:", gamma(S, K, T, r, sigma))
print("Vega:", vega(S, K, T, r, sigma))
