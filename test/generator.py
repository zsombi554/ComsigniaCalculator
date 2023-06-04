import random
import math


class RandomGenerator:
    size = 1000

    @staticmethod
    def _get_limits(number):
        maximum = round(math.log10(abs(number)), 0)
        minimum = maximum - 1
        return [1 + (10 ** minimum), 10 ** maximum]

    @classmethod
    def random_ints_in_range(cls, number):
        return random.randrange(*cls._get_limits(number))

    @classmethod
    def random_float_in_range(cls, number):
        return round(random.uniform(*cls._get_limits(number)), 2)

    @classmethod
    def random_int_in_range_as_str(cls, number):
        return str(random.randrange(*cls._get_limits(number)))

    @classmethod
    def random_float_in_range_as_str(cls, number):
        return str(round(random.uniform(*cls._get_limits(number)), 2))

    @classmethod
    def get_x_random_ints(cls, x):
        return [random.randrange(1, int(cls.size)) for _ in range(x)]

    @classmethod
    def get_x_random_floats(cls, x):
        return [random.uniform(1, cls.size) for _ in range(x)]


class TestInputGenerator:
    ranges = (10, 100, 1000, 10000, 100000)

    @classmethod
    def ints(cls, negative=False, zero=False):
        values = cls.positive_int()
        if negative:
            values += cls.neg_int()

        if zero:
            values.insert(0, 0)

        return values

    @classmethod
    def floats(cls, negative=False, zero=False):
        values = cls.positive_float()
        if negative:
            values += cls.neg_float()

        if zero:
            values.insert(0, 0.0)
            values = values[:-1]

        return values

    @classmethod
    def robust_ints(cls, case_num, negatives=False, zero=False):
        if negatives:
            case_num = case_num // 2

        cases = cls.positive_int_n(case_num)

        if negatives:
            cases += cls.neg_int_n(case_num)

        if zero:
            cases.insert(0, 0)
            cases = cases[:-1]

        return cases

    @classmethod
    def robust_floats(cls, case_num, negatives=False, zero=False):
        if negatives:
            case_num = case_num // 2

        cases = cls.positive_float_x(case_num)
        if negatives:
            cases += cls.negative_float_x(case_num)

        if zero:
            cases.insert(0, 0.0)
            cases = cases[:-1]

        return cases

    @classmethod
    def positive_int(cls):
        return [RandomGenerator.random_ints_in_range(_) for _ in cls.ranges]

    @classmethod
    def positive_float(cls):
        return [RandomGenerator.random_float_in_range(_) for _ in cls.ranges]

    @classmethod
    def neg_int(cls):
        return [-v for v in cls.positive_int()]

    @classmethod
    def neg_float(cls):
        return [-v for v in cls.positive_float()]

    @classmethod
    def positive_int_n(cls, x=100):
        return RandomGenerator.get_x_random_ints(x)

    @classmethod
    def neg_int_n(cls, x=100):
        return [-v for v in cls.positive_int_n(x)]

    @classmethod
    def positive_float_x(cls, x=100):
        return RandomGenerator.get_x_random_floats(x)

    @classmethod
    def negative_float_x(cls, x=100):
        return [-v for v in cls.positive_float_x(x)]

    @classmethod
    def positive_int_as_str(cls):
        return [str(v) for v in cls.positive_int()]

    @classmethod
    def bool_variables(cls):
        return [False, True]

    @classmethod
    def none_variable(cls):
        return [None]
