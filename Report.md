

<div style="text-align: center;">
    <span style="font-size:1.8rem;font-weight:Bold;">
ASSIGNMENT 6    </span>
</div><br/><br/> <br/> <br/> <br/> <br/>
<div style="text-align: center;">
    <span style="font-size:1.8rem;font-weight:Bold;">
ELP780 Software Lab    </span>
</div> <br/> <br/> <br/> <br/> <br/> <br/>
<div style="text-align: center;">
    <span style="font-size:1.7rem;font-weight:Bold;">
Kakul Shrivastava    </span>
</div> <br/>
<div style="text-align: center;">
    <span style="font-size:1.7rem;font-weight:Bold;">
2020EET2173    </span>
</div> <br/>
<div style="text-align: center;">
    <span style="font-size:1.7rem;font-weight:Bold;">
2020-2022    </span>
</div> <br/> <br/> <br/> <br/> <br/> <br/>
<div style="text-align: center;">
    <span style="font-size:1.7rem;">
A report presented for the assignment on    </span>
</div> <br/>
<div style="text-align: center;">
    <span style="font-size:1.7rem;font-weight:Bold;">
        Python Basics and Lex and Yacc
    </span>
</div> <br/><br/> <br/><br/> <br/> <br/> <br/><br/>
<div style="text-align: center;">
    <span style="font-size:1.5rem;font-weight:Bold;">
Department of Electrical Engineering    </span>
</div> <br/>
<div style="text-align: center;">
    <span style="font-size:1.5rem;font-weight:Bold;">
IIT Delhi    </span>
</div> <br/>
<div style="text-align: center;">
    <span style="font-size:1.5rem;font-weight:Bold;">
India    </span>
</div><br/>
<div style="text-align: center;">
    <span style="font-size:1.5rem;font-weight:Bold;">
November 17, 2020    </span>
</div>












**Table of Contents**



[TOC]


























###  1. Problem Statement 1

#### 1.1 Objective :

- Given two non-zero numbers A and B, count the number of 1s in their binary representations and output if their bit balanced (number of 1s are equal) or bit biased (number of 1s are unequal)

#### 1.2 Algorithm and Implementation :

- **Function to calculate number of 1's in binary representation of a number :**

  - Initialisation :  count = 0 ( to store number of 1's)
  - 'AND' the number with '1' to get the LSB and add it to count (increment if it is '1' else remains same)
  - Right shift the number by 1 to get the next higher bit in the position of LSB
  - Repeat till the number is greater than 0 (has atleast one '1' in its representation)

- Take the input for both numbers

- Calculate the number of 1s in both numbers using the above function (Let the result be |A| and |B|)

- IF (|A|-|B| == 0):

  ​			print : Bit Balanced

- ELSE :

  ​			print : Bit Biased (|A| - |B|)

#### 1.3 Flowchart : 

#### 1.3.1 Function to calculate number of 1s in binary representation : 

```flow
st=>start: Start
1=>operation: Set count = 0 
2=>operation: 'AND' the number with '1' 
and add the result to count
3=>operation: Right shift the number by 1 
cond=>condition: Is number greater than 0?
4=>operation: Return count

st->1->2->3->cond
cond(no)->4
cond(yes)->2
```

#### 1.3.2 Main program :

```flow
st=>start: Start
1=>operation: Take input of both numbers
2=>operation: Calculate the number of 1s in both numbers using the above function 
(|A| and |B|)
cond=>condition: |A|-|B| == 0 
3=>operation: print : Bit Balanced
4=>operation: print : Bit Biased (|A| - |B|)

st->1->2->cond
cond(no)->4
cond(yes)->3
```



#### 1.4 Screenshots :

![](/home/kakul/Pictures/Screenshot from 2020-11-17 14-50-08.png)

​																													**Figure 1 : Results of PS1**															

### 2. Problem Statement 2

#### 2.1 Objective :

#### 2.2 Algorithm and Implementation :

#### 2.3 Screenshots :



​																											**Figure 2 : Results of PS2**

​																													**Figure 3 : Git log**

### 3. Appendix

#### 3.1 Code for Problem Statement 1

```python
#Function to calculate number of 1's in binary representation of a number

def count_ones(n):
    count=0         #Initializing count to store number of 1's 

    while(n>0):                 #Iterating till the number is greater than 0 (has atleast one '1' in its representation)
        count=count + (n & 1)   #'AND' the number with 1 to get the LSB and add it to count (increment if it is '1' else remains same)
        n=(n>>1)                #Right shift the number by 1 to get the next higher bit in the position of LSB

    return count                #Return the value of count after iteration is complete

a=int(input("Enter the first number: "))    #Take the input of first number
b=int(input("Enter the second number: "))   #Take the input of second number

A=count_ones(a)                             #Count number of 1s in first number
B=count_ones(b)                             #Count number of 1s in second number

#Printing the output in desired format

print("\n\t\t\tFirst Number (A) \tSecond Number(B) \tRemarks")
print("Binary Representation \t{}=\"{}\" \t\t{}=\"{}\" \t\t{} (||{}| - |{}|| = |{} - {}| = {})"
        .format(a,bin(a),b,bin(b),"Bit Balanced" if (A-B==0) else "Bit Biased",a,b,A,B,abs(A-B)))
```



#### 3.2 Code for Problem Statement 2

```bash
#!/bin/bash

echo "PART 1"
echo

#1: To generate separate text files of each year 
awk -f ps21.awk election_2000-2016.txt		#Executing awk file for Task 1

#2: To calculate total and percentage of votes secured and most popular candidate
awk -f ps22.awk 2016.txt			#Executing awk file for Task 2

echo 
echo "PART 2"
echo 

#1: To create swingstate.txt
awk -f ps23.awk 2016.txt			

echo 

#To calculate votes secured by each candidate and total number of votes in swing states in 2016 
awk -f ps24.awk swingstate.txt			

#To calculate total number of votes in 2016
awk -f ps25.awk 2016.txt

swing=$(sed -n '3p' votes.txt)		#Extracting votes secured in swing states
votes=$(sed -n '4p' votes.txt)		#Extracting total votes in 2016
total=$[(swing*100) / votes] 		#Calculating percentage of votes in swing states
echo
echo "Percentage of votes in swing states : $total "
echo

#Extracting the percentage of votes by each candidate and total votes in swing state and displaying
echo "|	Name 	  | Votes secured in %  | Out of votes in swing states |"
echo "| Hillary Clinton | $(sed -n '1p' votes.txt)		| $(sed -n '3p' votes.txt)			|"
echo "| Donald Trump	  | $(sed -n '2p' votes.txt)		| $(sed -n '3p' votes.txt)			|"

$(rm votes.txt)
```

### References

1. *Awk* , https://www.grymoire.com/Unix/Awk.html 
2. _Awk Tutorial_ , https://www.tutorialspoint.com/awk/index.htm
3. _The UNIX School - awk & sed_ , https://www.theunixschool.com/p/awk-sed.html
4. _15 Practical Grep Command Examples In Linux / UNIX_ , https://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/



