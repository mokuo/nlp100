from p07 import main


def test_main():
    expect = "12時の気温は22.4"
    assert main(12, "気温", 22.4) == expect
