import pytest
from test.generator import TestInputGenerator as tIG


@pytest.mark.calc_method('bshl')
@pytest.mark.i_calc_method('bit_shift_left')
class TestBshl:
    @staticmethod
    def bin(number):
        if isinstance(number, int):
            return ('{:0%db}' % (1 if number == 0 else number.bit_length())).format(number)

    @pytest.mark.key('int')
    @pytest.mark.parametrize('b', list(range(8)))
    @pytest.mark.parametrize('a', [2**7])
    def test_input_int(self, method, a, b):
        assert self.bin(method(a, b)) == self.bin(a << b), f'{self.bin(a)} << {b}'

    @pytest.mark.key('float')
    @pytest.mark.parametrize('a, b', list(zip(tIG.floats(negative=True, zero=True),
                                              tIG.floats(negative=True, zero=True))))
    def test_input_float(self, method, a, b):
        with pytest.raises(TypeError) as exc:
            method(a)
        assert exc.value

    @pytest.mark.key('neg')
    @pytest.mark.parametrize('b', tIG.neg_int())
    @pytest.mark.parametrize('a', tIG.ints(negative=False, zero=True))
    def test_negative_shift(self, method, a, b):
        with pytest.raises(ValueError) as exc:
            method(a, b)
        assert exc.value

    @pytest.mark.key('str')
    @pytest.mark.parametrize('a, b', list(zip(tIG.positive_int_as_str(),
                                              tIG.positive_int_as_str())))
    def test_input_str(self, method, a, b):
        with pytest.raises(TypeError) as exc:
            method(a)
        assert exc.value


    @pytest.mark.key('robust')
    @pytest.mark.parametrize('b', tIG.robust_ints(20, negatives=False, zero=True))
    @pytest.mark.parametrize('a', tIG.robust_ints(20, negatives=True, zero=True))
    def test_robust(self, method, a, b):
        assert self.bin(method(a, b)) == self.bin(a << b), f'{self.bin(a)} << {b}'

