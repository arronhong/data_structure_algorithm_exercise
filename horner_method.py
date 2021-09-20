def horner(poly, x):
    ret = poly[0]
    for i in range(1, len(poly)):
        ret = ret*x + poly[i]
    return ret


if __name__ == '__main__':
    assert -11 == horner([1, -4, 2, -1, 1], 3)
    assert 5 == horner([2, -6, 2, -1], 3)
    assert -1 == horner([-1], -1)
