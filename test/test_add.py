import pytest
from .generator import TestInputGenerator as tIG


@pytest.mark.calc_method('add')
@pytest.mark.i_calc_method('add')
class TestAdd:
    @pytest.mark.key('int')
    @pytest.mark.parametrize('a, b', list(zip(tIG.ints(negative=True, zero=True),
                                              tIG.ints(negative=True, zero=True))))
    def test_input_int(self, method, a, b):
        assert method(a, b) == a + b, f'{a + b}'

    @pytest.mark.key('float')
    @pytest.mark.parametrize('a, b', list(zip(tIG.floats(negative=True, zero=True),
                                              tIG.floats(negative=True, zero=True))))
    def test_input_float(self, method, a, b):
        assert method(a, b) == a + b, f'{a + b}'

    @pytest.mark.key('str')
    @pytest.mark.parametrize('a, b', list(zip(tIG.positive_int_as_str(),
                                              tIG.positive_int_as_str())))
    def test_input_str(self, method, a, b):
        assert method(a, b) == int(a) + int(b), f'{a} + {b} both str'

    @pytest.mark.key('robust')
    @pytest.mark.parametrize('b',
                             tIG.robust_ints(case_num=10, negatives=True, zero=True) +
                             tIG.robust_floats(case_num=10, negatives=True, zero=True))
    @pytest.mark.parametrize('a',
                             tIG.robust_ints(case_num=10, negatives=True, zero=True) +
                             tIG.robust_floats(case_num=10, negatives=True, zero=True))
    def test_robust(self, method, a, b):
        assert method(a, b) == a + b, f'{a + b}'
