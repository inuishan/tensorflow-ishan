__author__ = 'ishan'
__time__ = '28/11/16'

x = 1000000000
for i in range(0, 1000000):
	x += 0.000001
x = x - 1000000000
print(x)