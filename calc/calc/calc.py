from functools import reduce


class Calc():

    def add(self, *args):
        return sum(args)

    def sub(self, a , b ):
        return a - b

    def mul(self, *args):
        def mul2(a, b):
            return a * b

        return reduce(mul2, args)
