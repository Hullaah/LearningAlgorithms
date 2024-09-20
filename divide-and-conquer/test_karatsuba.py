from karatsuba import karatsuba


def test_karatsuba():
    """
    Tests the karatsuba multiplication algorithm
    """
    assert karatsuba(123456, 78910) == 123456 * 78910
    assert karatsuba(999103, 180) == 999103 * 180
    assert karatsuba(99999, 9999) == 99999 * 9999
    assert karatsuba(
        3141592653589793238462643383279502884197169399375105820974944592,
        2718281828459045235360287471352662497757247093699959574966967627,
    ) == (
        3141592653589793238462643383279502884197169399375105820974944592
        * 2718281828459045235360287471352662497757247093699959574966967627
    )
