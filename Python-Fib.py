#William Purcell
#Python Fibonacci Sequence
#Complexity: (n)
#2/6/2024

def fib_nonrecursive ( fib_Iteration):   #Define Fibonacci Function
    Fib_1,Fib_2,fib_compute =0,1,abs(fib_Iteration) #Define Variable, First Element, Second Element, and a variable used to compute the result
    
    for i in range(fib_compute): #Comput Result of the Fib Sequence
        Fib_1,Fib_2 = Fib_2, Fib_1+Fib_2
    
    if fib_Iteration>=0 :   #Check if the original function was negative
        return Fib_1        #Return Positive Results
    return -Fib_1           #Return Negative Results
       
      
IsInt = 0           #Variable Used to hold the int check loop 
while(IsInt!= 1): #Integer Check Loop
    try:            #Try to define the User Input as an Int
        Num_Iteration= int(input ("What iteration of the Fibonacci Sequence would you like? ")) #Try to Define user Iput as an integer "Num_Iteration"
        IsInt=1     #If assignment was successful increment "IsInt" breaking the loop

    except ValueError:
        print("Invalid Entry. Please enter a whole number")   #If unable to define UI as an int let them know and prompt for a new number


print("The Fibonacci Sequence is ", fib_nonrecursive(Num_Iteration)) #Print the Fibonacci Result by calling the fib_nonrecursive in a print statement


