def fibo(x):
    a,b=0,1
    while b < x :
			c=b
			b=a+b
			a=c
			print(a, end=' ')
            
fibo(2000)
f=fibo
print('\n')
f(200)
