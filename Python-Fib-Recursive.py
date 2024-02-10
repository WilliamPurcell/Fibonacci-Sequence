#William Purcell
#Python Fibonacci Recursive Sequence
#Complexity: (exponential)
#2/9/2024

def fib_recursive (fib_Iteration):      #Define Fibonacci Function
    fib_compute =abs(fib_Iteration)     #Define Variable, First Element, Second Element, and a variable used to compute the result
    
    if (fib_compute==0 or fib_compute ==1):
        return fib_compute
    out1 = fib_recursive(fib_compute-1) #Call the original Function to find the previous 2 numbers
    out2 = fib_recursive(fib_compute-2)
    if fib_Iteration>=0 :   #Check if the original function was negative
        return out1+ out2   #Return Positive sum of the last two numbers Results
    return -(out1+ out2 )   #Return Negative sum of the last two numbers Results

      
IsInt = 0           #Variable Used to hold the int check loop 
while(IsInt!= 1):   #Integer Check Loop
    try:            #Try to define the User Input as an Int
        Num_Iteration= int(input ("What iteration of the Fibonacci Sequence would you like? ")) #Try to Define user Iput as an integer "Num_Iteration"
        IsInt=1     #If assignment was successful increment "IsInt" breaking the loop

    except ValueError:
        print("Invalid Entry. Please enter a whole number")   #If unable to define UI as an int let them know and prompt for a new number

print("The Fibonacci Sequence is ", fib_recursive(Num_Iteration)) #Print the Fibonacci Result by calling the fib_nonrecursive in a print statement