import pytest
from .generator import TestInputGenerator as tIG


@pytest.mark.calc_method('band')
@pytest.mark.i_calc_method('bit_and')
class TestBand:
    @staticmethod
    def bin(number):
        if isinstance(number, int):
            return ('{:0%db}' % (1 if number == 0 else number.bit_length())).format(number)

    @pytest.mark.key('int')
    @pytest.mark.parametrize('b', [2 ** i for i in range(8)])
    @pytest.mark.parametrize('a', [sum([2 ** i for i in range(8)])])
    def test_input_int(self, method, a, b):
        assert self.bin(method(a, b)) == self.bin(a & b), f'{self.bin(a)} & {self.bin(b)}'

    @pytest.mark.key('float')
    @pytest.mark.parametrize('a, b', list(zip(tIG.floats(negative=True, zero=True),
                                              tIG.floats(negative=True, zero=True))))
    def test_input_float(self, method, a, b):
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
    @pytest.mark.parametrize('b', tIG.robust_ints(case_num=20, negatives=True, zero=True))
    @pytest.mark.parametrize('a', tIG.robust_ints(case_num=20, negatives=True, zero=True))
    def test_robustness(self, method, a, b):
        assert self.bin(method(a, b)) == self.bin(a & b), f'{self.bin(a)} & {self.bin(b)}'
