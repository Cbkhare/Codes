from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.run()

'''
gr2 = greenlet(test2)
gr1 = greenlet(run=test1,parent=gr2)
gr1.switch()
Output:
12
56
34
78  # execution returned to parent
'''


'''
gr1 = greenlet(run=test1)
gr2 = greenlet(test2)
gr1.switch()
Output:
12
56
34

Note:- 78 was not printed
'''

'''
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
12
56
34


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.run()
12
56
12
78
34
'''