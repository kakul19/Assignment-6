#Function to calculate number of 1's in binary representation of a number

def count_ones(n):
    count=0         #Initializing count to store number of 1's 

    while(n>0):                 #Iterating till the number is greater than 0 (has atleast one '1' in its representation)
        count=count + (n & 1)   #'AND' the number with number to get the LSB and add it to count (increment if it is '1' else remains same)
        n=(n>>1)                #Right shift the number by 1 to get the next higher bit in the position of LSB

    return count                #Return the value of count after iteration is complete

a=int(input("Enter the first number: "))    #Take the input of first number
b=int(input("Enter the second number: "))   #Take the input of second number

A=count_ones(a)                             #Calculate number of 1s in first number
B=count_ones(b)                             #Calculate number of 1s in second number

#Printing the output in desired format

print("\n\t\t\tFirst Number (A) \tSecond Number(B) \tRemarks")
print("Binary Representation \t{}=\"{}\" \t\t{}=\"{}\" \t\t{} (||{}| - |{}|| = |{} - {}| = {})"
        .format(a,bin(a),b,bin(b),"Bit Balanced" if (A-B==0) else "Bit Biased",a,b,A,B,abs(A-B)))
