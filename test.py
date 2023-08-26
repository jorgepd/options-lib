# imports
from src.models import bsm, implied_vol
import numpy as np
from scipy.stats import norm

N_prime = norm.pdf
N = norm.cdf



def BS_CALLDIV(S, K, T, r, q, sigma):
    d1 = (np.log(S/K) + (r - q + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return S*np.exp(-q*T) * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUTDIV(S, K, T, r, q, sigma):
    d1 = (np.log(S/K) + (r - q + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*np.exp(-q*T)*N(-d1)

s = 100
x_ls = list(x for x in range(90, 111, 10))
t_ls = [0.5, 1]
r_ls = [0.05, 0.1]
v_ls = [0.2, 0.3, 0.4]

for x in x_ls:
    for t in t_ls:
        for r in r_ls:
            for v in v_ls:
                print('-----')
                print(s, x, t, r, v)
                print(BS_CALLDIV(s, x, t, r, 0, v))


