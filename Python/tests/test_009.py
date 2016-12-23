import challenges.challenge_009 as ch9

def test_009():
    expected = 60
    actual = ch9.main(12)
    assert(expected == actual)

    expected = 31875000
    actual = ch9.main(1000)
    assert(expected == actual)
