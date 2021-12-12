def test( i):
    i += 1
    print( i)
    if i == 5:
        return
    else:
        test( i)
        print( i)
test(0)
