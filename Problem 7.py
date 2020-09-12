numberOfPrimes = 0
currentNumber = 1
isPrime = True

while numberOfPrimes != 10001:

    currentNumber+=1
    isPrime = True

    for i in range(2, currentNumber):
        if currentNumber%i==0:
            isPrime = False
            break

    if isPrime == True:
        numberOfPrimes+=1

print(currentNumber)
