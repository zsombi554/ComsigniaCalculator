import pytest
from .generator import TestInputGenerator as tIG


@pytest.mark.calc_method('bnot')
@pytest.mark.i_calc_method('bit_not')
class TestBnot:
    @staticmethod
    def bin(number):
        if isinstance(number, int):
            return ('{:0%db}' % (1 if number == 0 else number.bit_length())).format(number)

    @pytest.mark.key('int')
    @pytest.mark.parametrize('a', [2**i for i in range(8)])
    def test_input_int(self, method, a):
        assert self.bin(method(a)) == self.bin(~a), f'~{self.bin(a)}'

    @pytest.mark.key('float')
    @pytest.mark.parametrize('a', tIG.floats(negative=True, zero=True))
    def test_input_float(self, method, a):
        with pytest.raises(TypeError) as exc:
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
    @pytest.mark.parametrize('a', tIG.robust_ints(case_num=100, negatives=True, zero=True))
    def test_robust(self, method, a):
        assert self.bin(method(a)) == self.bin(~a), f'~{self.bin(a)}'

