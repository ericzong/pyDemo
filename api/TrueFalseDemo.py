def truth_test(x):
    if x:
        return True
    else:
        return False


class X:
    pass


class Y:
    def __bool__(self):
        return False


class Z:
    def __len__(self):
        return 0


class YY:
    def __bool__(self):
        return False

    def __len__(self):
        return 1


class ZZ:
    def __bool__(self):
        return True

    def __len__(self):
        return 0


if __name__ == '__main__':
    x = X()
    y = Y()
    z = Z()
    yy = YY()  # __bool__ 和 __len__ 均实现，以前者为准
    zz = ZZ()

    print(truth_test(x))
    print(truth_test(y))
    print(truth_test(z))
    print(truth_test(yy))
    print(truth_test(zz))

    print(truth_test(None))
    print(truth_test(False))
    print(truth_test(0))
    print(truth_test(0.0))
    print(truth_test(0j))  # 复数
    from decimal import Decimal

    print(truth_test(Decimal(0)))  # 十进制浮点数
    from fractions import Fraction

    print(truth_test(Fraction(0, 1)))  # 分数
    print(truth_test(''))
    print(truth_test(()))
    print(truth_test({}))
    print(truth_test(set()))
    print(truth_test(range(0)))
