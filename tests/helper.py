

def assert_with_tol(a, b, tol=1e-5):
    diff = abs(a - b)
    pct_diff = diff / min(a, b)
    print(f'{a} and {b} have a {pct_diff * 100}% difference!')
    assert(pct_diff < tol)


def assert_call_put(fun, p, a, b, tol=1e-5):
    assert_with_tol(fun('C', *p)[0], a, tol)
    assert_with_tol(fun('P', *p)[0], b, tol)


def assert_impl_vol(fun, opt, p, val, tol=1e-5):
    obs_p = opt('C', *p, val)[0]
    assert_with_tol(fun(opt, 'C', *p, obs_p), val, tol)
    obs_p = opt('P', *p, val)[0]
    assert_with_tol(fun(opt, 'P', *p, obs_p), val, tol)

