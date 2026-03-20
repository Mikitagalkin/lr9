import fastmath

def test_sum_squares():
    assert fastmath.sum_squares([1, 2, 3, 4, 5]) == 55

def test_point():
    p1 = fastmath.Point(0, 0)
    p2 = fastmath.Point(3, 4)
    assert p2.distance(p1) == 5.0
    assert p1.x == 0 and p1.y == 0