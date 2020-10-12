from calc.calc import Calc

def test_add_two_numbers():
    c = Calc()

    res = c.add(4,5)

    assert res == 9


def test_add_three_numbers():

    c = Calc()

    res = c.add(1,2,3)

    assert res == 6


def test_add_many_number():
    s = range(100)

    assert Calc().add(*s) == 4950


def test_subtract_two_numbers():
    c = Calc()

    res = c.sub(10, 3)

    assert res == 7
