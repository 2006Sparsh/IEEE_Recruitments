n = int(input("Enter the number of rows you want in the star pattern : "))

for i in range(1,n+1): #since range goes from 1st number to the second number-1, we keep it as 1,n+1 and not 1,n
    print(" "*(n-i) + "*"*i) #this prints space , n-1 times; and then an asterisk i times, this is due to the specific pattern asked in the question
    # if we want the asterisks to start from left hand side, we can skip the spacebar printing 
    