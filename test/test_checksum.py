import pytest
from test.generator import TestInputGenerator as tIG


@pytest.mark.calc_method('checksum')
@pytest.mark.i_calc_method(None)
class TestChecksum:
    @pytest.mark.key('int')
    @pytest.mark.parametrize('a', tIG.ints(negative=False, zero=True))
    def test_input_int(self, method, a):
        assert method(a) != 0

    @pytest.mark.key('float')
    @pytest.mark.parametrize('a', tIG.floats(negative=False, zero=True))
    def test_input_float(self, method, a):
        with pytest.raises(TypeError) as exc:
            method(a)
        assert exc.value

    @pytest.mark.key('neg')
    @pytest.mark.parametrize('a', tIG.neg_int() + tIG.neg_float())
    def test_negatives(self, method, a):
        with pytest.raises(ValueError) as exc:
            method(a)
        assert exc.value

    @pytest.mark.key('robust')
    @pytest.mark.parametrize('a', tIG.robust_ints(case_num=400, negatives=False, zero=True))
    def test_robust(self, method, a):
        assert method(a) != 0
