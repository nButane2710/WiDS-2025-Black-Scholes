from src.black_scholes import call_price, put_price
from src.greeks import delta_call, gamma, vega
from src.monte_carlo import monte_carlo_call
from src.implied_volatility import implied_volatility_call

S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

call_bs = call_price(S, K, T, r, sigma)
put_bs = put_price(S, K, T, r, sigma)
call_mc = monte_carlo_call(S, K, T, r, sigma)
iv = implied_volatility_call(call_bs, S, K, T, r)

print("Black–Scholes Call:", call_bs)
print("Black–Scholes Put :", put_bs)
print("Monte Carlo Call  :", call_mc)

print("Call Delta:", delta_call(S, K, T, r, sigma))
print("Gamma     :", gamma(S, K, T, r, sigma))
print("Vega      :", vega(S, K, T, r, sigma))

print("Implied Volatility:", iv)
