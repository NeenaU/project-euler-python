#Loop through numbers from 0-999
#Check if each number is a multiple of 3 or 5
#If so, add it to the result

result = 0

for i in range(1000):
    if (i%3==0 or i%5==0):
        result += i

print(result)
