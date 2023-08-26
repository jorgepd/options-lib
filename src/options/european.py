# custom imports
from src.models import bsm, implied_vol
from .base import BaseOption



class EuropeanOption(BaseOption):
    '''
    This class represents an European option, and uses the Black
    Scholed model formula to calculate option prices and the Greeks.
    Implied volatility is calculated using the Newton-Raphson method.

    Refer to base class for parameter descriptions.
    '''

    def __init__(self, opt_type, s, x, t, r, v):
        super().__init__(opt_type, s, x, t, r, v)


    def calc_values(self):
        value, delta, gamma, vega, theta, rho = bsm.black_scholes(
            self.opt_type, self.s, self.x, self.t, self.r, self.v
        )
        self.value = value
        self.delta = delta
        self.gamma = gamma
        self.vega = vega
        self.theta = theta
        self.rho = rho

        return value, delta, gamma, vega, theta, rho


    def calc_implied_vol(self, p):
        v = implied_vol.newton_raphson_search(
            bsm.black_scholes, self.opt_type, self.s, self.x, self.t, self.r, p
        )

        # did not converge, try other method
        if v == -1:
            v = implied_vol.bisection_search(
                self.opt_type, self.s, self.x, self.t, self.r, self.v
            )
        
        self.v = v
        return v

