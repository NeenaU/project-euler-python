sumOfSquares = 0
sumOfNumbers = 0

for num in range (1, 101):
    sumOfSquares += num**2
    sumOfNumbers += num

squareOfSum = sumOfNumbers**2
print(squareOfSum - sumOfSquares)
