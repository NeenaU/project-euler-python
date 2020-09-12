numberOfDivisors = 0
currentNumber = 0
count = 1
overFiveHundred = False

while overFiveHundred == False:

    currentNumber += count
    numberOfDivisors = 0
    end = 0

    if currentNumber%2==0:
        end = currentNumber/2+1

    else:
        end = (currentNumber+1)/2

    end = int(end)
    
    for num in range(1, end):
        if currentNumber%num == 0:

            numberOfDivisors+=1

    numberOfDivisors+=1

    if numberOfDivisors > 100:
        overFiveHundred = True
    
    count+=1

print(currentNumber)
