def test(r):
    p = len(r)
    return r[-1] == "!" and r[:-1]== (p / 2) * "ha"
