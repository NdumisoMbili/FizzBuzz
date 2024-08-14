# Given number n
# Iterate from 1 to n... In this case from 1 to 100
# If the current value is divisible by 3 print "Fizz"
# If the current value is divisible by 5 print "Buzz"
# If the current value is divisible by both 3 and 5 print "FizzBuzz" 
# If the current value does not satisfy any of the conditions print out the value

def fizzBuzz(n):

    for i in range (1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print   ("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
            
fizzBuzz(100)