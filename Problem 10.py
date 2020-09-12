sumOfPrimes = 0
num = 3

while num < 2000000:

    isPrime = True
    
    if (num%2!=0):
        i=2
        while i != num:
            if num%i==0:
                isPrime = False
                break

            i+=1

        if isPrime == True:
            sumOfPrimes += num

    num+=2

print(sumOfPrimes)

        
