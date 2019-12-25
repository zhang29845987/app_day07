import pytest, os, sys

sys.path.append(os.getcwd())

from Base.getDatas import GetData


def data_ss():
    cs = []
    s = GetData()
    s = s.get_datas("xx.yaml")
    for aa in s:
        r = aa.values()
        cs.append(tuple(r))
    print(cs)
    return cs


class Test01:
    @pytest.mark.parametrize("a,b,c", data_ss())
    def test_01(self, a, b, c):
        assert a + b == c
