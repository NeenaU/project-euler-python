numberFound = False
currentNumber = 1

while(numberFound == False):

    if (str(currentNumber)[len(str(currentNumber))-1] == "0"):
        for num in range(1, 21):

            if (currentNumber%num != 0):
                currentNumber += 1
                break

            elif (currentNumber%num == 0 and num == 20):
                numberFound = True

print(currentNumber)
