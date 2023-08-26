# imports
from abc import ABC, abstractmethod

# custom imports
from src.models.implied_vol import MIN_VOL, MAX_VOL



class BaseOption(ABC):
    '''
    Standard interface for option classes.

    Parameters:
    opt_type - 'C' for call, or 'P' for put
    s - spot price of underlying
    x - strike price
    t - time to maturity, in years
    r - risk-free interest rate
    v - implied volatility
    '''

    def __init__(self, opt_type, s, x, t, r, v):
        # inputs
        self.opt_type = opt_type.upper()
        self.s = s
        self.x = x
        self.t = t
        self.r = r
        self.v = v

        # input limits
        self._validate_inputs()
    

    def _validate_inputs(self):
        # option type
        if self.opt_type not in ['C', 'P']:
            raise ValueError('Option type should be either a \'C\' or a \'P\'!')
        
        # spot price
        # 1 cent
        # a high enough cap to prevent bad input
        self._validate_values(self.s, 'Spot price', 0.01, 9000000)
        
        # strike
        # same as above
        self._validate_values(self.x, 'Strike', 0.01, 9000000)
        
        # time to maturity
        # at least an hour before expiry
        # nobody lives to see the expiry of an option with 100 years until maturity
        self._validate_values(self.t, 'Time to maturity', 1/(24*252), 100)
        
        # risk free rate
        # user probably tried to input a value like 10% and entered 10 instead of 0.1
        self._validate_values(self.r, 'Spot price', -1, 2)
        
        # spot price
        # same as above
        self._validate_values(self.v, 'Spot price', MIN_VOL, MAX_VOL)


    def _validate_values(self, value, name, min_v, max_v):
        if (
            (value < min_v)
            or (value > max_v)
        ):
            raise ValueError(f'{name} values should range between {min_v} and {max_v}!')


    @abstractmethod
    def calc_values(self):
        raise NotImplementedError('Should implement calc_values()!')


    @abstractmethod
    def calc_implied_vol(self):
        raise NotImplementedError('Should implement calc_implied_vol()!')

