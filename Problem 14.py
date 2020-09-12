longestChain = 0
num = 1
result = 0

def generateNumber(number):

    result = 0
    
    if number%2 == 0:
        result = number/2

    else:
        result = 3*number+1

    return result

while num < 999999:
    
    num += 1
    chain = 1
    currentNumber = generateNumber(num)
    
    while currentNumber != 1:
        currentNumber = generateNumber(currentNumber)
        chain += 1

    if chain > longestChain:
        longestChain = chain
        result = num
    

print(result)
