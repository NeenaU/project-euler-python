#List of all prime factors for the number
primeFactors = []

#Result of multiplying all prime factors currently found
calculation = 0

#Number itself
number = 600851475143

#Current number to test if prime and a prime factor
currentNumber = 2;

#Whether the current number is prime
isPrime = False;

'''Function to check if all prime factors have been found'''
def checkFactors():
    result = 1
    for i in primeFactors:
        result *= i;
    return result

while (calculation != number):

    #Check if current number is prime
    for i in range(2, currentNumber):
        if (currentNumber%i == 0):
            isPrime = True

    #If current number is a prime factor, add it to list of prime factors
    #and check if all prime factors have been found
    if (isPrime and number%currentNumber==0):
        primeFactors.append(currentNumber)
        calculation = checkFactors()

    currentNumber+=1

print(primeFactors[len(primeFactors)-1])
