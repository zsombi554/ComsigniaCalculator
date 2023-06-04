import pytest
from .generator import TestInputGenerator as tIG
from math import sqrt


@pytest.mark.calc_method('sqrt')
@pytest.mark.i_calc_method('sqrt')
class TestSqrt:
    @pytest.mark.key('int')
    @pytest.mark.parametrize('a', tIG.ints(negative=False, zero=True))
    def test_input_int(self, method, a):
        assert method(a) == sqrt(a), f'{sqrt(a)}'

    @pytest.mark.key('float')
    @pytest.mark.parametrize('a', tIG.floats(negative=False, zero=True))
    def test_input_float(self, method, a):
        assert method(a) == sqrt(a), f'{sqrt(a)}'

    @pytest.mark.key('neg')
    @pytest.mark.parametrize('a', tIG.neg_int() + tIG.neg_float())
    def test_negatives(self, method, a):
        with pytest.raises(ValueError) as exc:
            method(a)
        assert exc.value

    @pytest.mark.key('str')
    @pytest.mark.parametrize('a, b', list(zip(tIG.positive_int_as_str(),
                                              tIG.positive_int_as_str())))
    def test_input_str(self, method, a, b):
        with pytest.raises(TypeError) as exc:
            method(a)
        assert exc.value


    @pytest.mark.key('robust')
    @pytest.mark.parametrize('a', tIG.robust_ints(case_num=200, negatives=False, zero=True) +
                             tIG.robust_floats(case_num=200, negatives=False, zero=True))
    def test_robust(self, method, a):
        assert method(a) == sqrt(a), f'{sqrt(a)}'

