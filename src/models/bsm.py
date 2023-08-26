# imports
from scipy.stats import norm
import math



def black_scholes(opt_type, s, x, t, r, v):
    '''
    Black Scholes model to calculate option prices and the Greeks.

    Parameters:
    opt_type - 'C' for call, or 'P' for put
    s - spot price of underlying
    x - strike price
    t - time to maturity, in years
    r - risk-free interest rate
    v - implied volatility
    '''

    # pre calculations
    sqrt_t = math.sqrt(t)
    d1 = (math.log(s / x) + (r + v**2/2) * t) / (v * sqrt_t)
    d2 = d1 - v * sqrt_t

    # call
    N_d1 = norm.cdf(d1)
    N_d2 = norm.cdf(d2)

    # put
    if opt_type == 'P':
        # -N(-d) = N(d) - 1
        N_d1 = N_d1 - 1
        N_d2 = N_d2 - 1

    N_d1_dx = norm.pdf(d1)
    e_rt = math.exp(-r * t)

    # value and greeks
    value = N_d1 * s - N_d2 * x * e_rt
    delta = N_d1
    gamma = N_d1_dx / (s * v * sqrt_t)
    vega = s * N_d1_dx * sqrt_t
    theta = -(s * N_d1_dx * v) / (s * sqrt_t) - r * x * e_rt * N_d2
    rho = x * t * e_rt * N_d2

    return value, delta, gamma, vega, theta, rho

