

# the number we will perform the collatz operations on
n = 20                 # Starting

# Keep looping until we reach one
# Note: this assumes that the collatz conjeture is true 
while n != 1:          # Condition for while loop 
    
    # Print the current value of n 
    print (n) 

    # Check if n is even 
    if n % 2 == 0      # This % sign states that if you divide n by 2 and if the remainder is zero then it is even 
        
    # If n is even divide it by 2   
        # n = n /2 or n /= 2   # the latter is shorthand for the same thing
        n = n /2 
    else:
    
    # if n is odd multiply it by 3 and add 1
        n = (3 * n) + 1
 
# Finally print one 
print (n)