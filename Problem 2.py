#Previous number in the sequence
previous = 1

#Current number in the sequence
current = 2

#Number after the current number in the sequence, a temp variable
after = 0

#The sum of even numbers
result = 0

#Loop until the value exceeds 4 million
#If the value is even, add it to the result
while (current <= 4000000):

    if (current%2==0):
        result += current

    after = current+previous
    previous = current
    current = after


print(result)
