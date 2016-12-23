import challenges.challenge_008 as ch8

def test_008():
    expected = 5832
    actual = ch8.main(4)
    assert(expected == actual)
    
    expected = 23514624000
    actual = ch8.main(13)
    assert(expected == actual)
