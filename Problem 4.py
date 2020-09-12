#Used to hold the largest palindrome found
largestPalindrome = 0

#Function used to compare digits for equality
def compareDigits():

    global a
    global b
    global result
    
    if (str(result)[a]==str(result)[b]):
        a+=1
        b-=1
        return True
    else:
        return False

for i in range(100, 1000):
    for j in range (100, 1000):

        result = i*j

        a=0
        b=len(str(result))-1

        #Even number of digits
        if (len(str(result))%2 == 0):
            
            for num in range(int(len(str(result))/2)+1):

                if (compareDigits() == False):
                    break
                    
                if (num == int(len(str(result))/2) and result > largestPalindrome):
                    largestPalindrome = result

        #Odd number of digits
        else:
            for num in range(int( (len(str(result))-1) /2)+1):

                if (compareDigits() == False):
                    break
                    
                if (num == int(len(str(result))-1/2) and result > largestPalindrome):
                    largestPalindrome = result


print(largestPalindrome)
