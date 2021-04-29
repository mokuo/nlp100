from p06 import main


def test_main():
    x_str = "paraparaparadise"
    y_str = "paragraph"

    expect = [
        {"pa", "ar", "ra", "ap", "ad", "di", "is", "se", "ag", "gr", "ph"},
        {"pa", "ar", "ra", "ap"},
        {"ad", "di", "is", "se"},
        True,
        False
    ]

    assert expect == main(x_str, y_str)
