# global parameters
MIN_VOL = 0.005
MAX_VOL = 2



def newton_raphson_search(fun, opt_type, s, x, t, r, p, tol=1e-5, max_steps=5000):
    '''
    Calculates Implied Volatility using the Newton-Raphson method.
    Works best when the strike is not further than 20% from the
    asset price. Only works for European options, which have a
    reliable Vega estimate.

    Parameters:
    fun - function to be used to calculate option price and Vega
    opt_type - 'C' for call, or 'P' for put
    s - spot price of underlying
    x - strike price
    t - time to maturity, in years
    r - risk-free interest rate
    p - option price
    tol - minimum price tolerance to stop calculations
    max_steps - max number of iterations
    '''

    # estimate a starting point
    v = 0.3
    last_diff = p

    # start the search
    for _ in range(max_steps):

        # calc option value
        value, _, _, vega, _, _ = fun(opt_type, s, x, t, r, v)
        diff = abs(value - p)

        # volatility out of bounds
        if (v > MAX_VOL) or (v < MIN_VOL):
            break

        # not converging
        if diff >= last_diff:
            break

        # return if deviation is smaller than tolerance
        if diff < tol:
            return v
        
        # i++
        v = v - (value - p) / vega
        last_diff = diff
    
    # did not converge
    print('-----', diff, last_diff)
    return -1


def bisection_search(fun, opt_type, s, x, t, r, p, tol=1e-5, max_steps=5000):
    '''
    Calculates Implied Volatility using the bisection method.
    Slower, but also works for American options, when there is
    no reliable Vega estimate.

    Parameters:
    fun - function to be used to calculate option price and Vega
    opt_type - 'C' for call, or 'P' for put
    s - spot price of underlying
    x - strike price
    t - time to maturity, in years
    r - risk-free interest rate
    p - option price
    tol - minimum price tolerance to stop calculations
    max_steps - max number of iterations
    '''

    # starting point
    v_low = MIN_VOL
    v_high = MAX_VOL

    # start the search
    for _ in range(max_steps):

        # calc option value
        v_mid = (v_high + v_low) / 2
        p_mid, _, _, _, _, _ = fun(opt_type, s, x, t, r, v_mid)
        diff = abs(p_mid - p)

        # return if deviation is smaller than tolerance
        if diff < tol:
            return v_mid

        # i++
        if p_mid > p:
            v_high = v_mid
        else:
            v_low = v_mid

    # max iterations, return best estimate
    return v_mid

