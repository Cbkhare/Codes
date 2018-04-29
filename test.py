def rat():
    r = True
    try:
        print ('asd')
        raise TypeError
        print (123)
        print (234234)
    except TypeError as e:
        r = False
    return r

if rat():
    print (True)
else:
    print (False)
