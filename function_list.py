def fun(a, b, c, *x):
    print('This a: %s' % a)
    print('This b: %s' % b)
    print('This c: %s' % c)
    y=list(x)
    print('This x: %s' % y)
    
fun('aa', 'bb', 'cc', 'p', 'q', 'r')
