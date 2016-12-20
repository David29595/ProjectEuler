import challenges.challenge_003 as ch3

def test_003():
    expected = 6857
    actual, factors = ch3.main(600851475143)
    assert(expected == actual)
