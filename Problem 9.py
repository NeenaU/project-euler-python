numbersFound = False
a = 0
b = 0
c = 0

while numbersFound == False:

    for i in range(3, 1000):
        for j in range(4, 1000):
            for k in range(5, 1000):

                if i+j+k==1000 and i**2+j**2==k**2:
                    a=i
                    b=j
                    c=k
                    numbersFound = True

product = a*b*c
print(a)
print(b)
print(c)
print(product)
