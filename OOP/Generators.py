import math
def Generator(a):
    i = 0
    while i <= a:
        yield math.factorial(i)
        i+=1
for j in Generator(10):
    print(j)