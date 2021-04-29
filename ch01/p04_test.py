from p04 import main


def test_main():
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    expect = dict(H=0, He=1, Li=2, Be=3, B=4, C=5, N=6, O=7, F=8, Ne=9,
                  Na=10, Mi=11, Al=12, Si=13, P=14, S=15, Cl=16, Ar=17, K=18, Ca=19)
    assert main(str) == expect
