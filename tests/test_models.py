# custom imports
from src.models.bsm import *
from src.models.implied_vol import *
from .helper import assert_with_tol, assert_call_put, assert_impl_vol



def test_bsm():
    # different s
    p = [90, 100, 1, 0.1, 0.3]
    assert_call_put(black_scholes, p, 10.51985812604488, 11.003599929640835)
    p = [100, 100, 1, 0.1, 0.3]
    assert_call_put(black_scholes, p, 16.73413358238666, 7.217875385982609)
    p = [110, 100, 1, 0.1, 0.3]
    assert_call_put(black_scholes, p, 24.129800450897115, 4.613542254493062)

    # different x
    p = [100, 90, 1, 0.1, 0.3]
    assert_call_put(black_scholes, p, 22.510077370599106, 3.945444993835462)
    p = [100, 110, 1, 0.1, 0.3]
    assert_call_put(black_scholes, p, 12.131028958035898, 11.663144941991447)
    
    # different t
    p = [100, 100, 0.5, 0.1, 0.3]
    assert_call_put(black_scholes, p, 10.906499852007414, 6.029442302078813)
    
    # different r
    p = [100, 100, 1, 0.05, 0.3]
    assert_call_put(black_scholes, p, 14.231254785985819, 9.354197236057232)
    
    # different v
    p = [100, 100, 1, 0.1, 0.2]
    assert_call_put(black_scholes, p, 13.269676584660893, 3.753418388256833)
    p = [100, 100, 1, 0.1, 0.4]
    assert_call_put(black_scholes, p, 20.318469310058703, 10.80221111365465)


def test_implied_vol():
    # newton raphson
    p = [100, 100, 1, 0.1]
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.2)
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.3)
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.4)
    p = [100, 85, 1, 0.1]
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.2)
    p = [100, 90, 1, 0.1]
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.2)
    p = [100, 110, 1, 0.1]
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.2)
    p = [100, 115, 1, 0.1]
    assert_impl_vol(newton_raphson_search, black_scholes, p, 0.2)

    # bisection
    p = [100, 100, 1, 0.1]
    assert_impl_vol(bisection_search, black_scholes, p, 0.2)
    assert_impl_vol(bisection_search, black_scholes, p, 0.3)
    assert_impl_vol(bisection_search, black_scholes, p, 0.4)
    p = [100, 80, 1, 0.1]
    assert_impl_vol(bisection_search, black_scholes, p, 0.2)
    p = [100, 90, 1, 0.1]
    assert_impl_vol(bisection_search, black_scholes, p, 0.2)
    p = [100, 110, 1, 0.1]
    assert_impl_vol(bisection_search, black_scholes, p, 0.2)
    p = [100, 120, 1, 0.1]
    assert_impl_vol(bisection_search, black_scholes, p, 0.2)
