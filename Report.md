

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
2=>operation: Calculate the number of 1s in both 
numbers using the above function (|A|,|B|)| 
cond=>condition: |A|-|B| == 0 |
3=>operation: print : Bit Balanced
4=>operation: print : Bit Biased (|A| - |B|)|

st->1->2->cond
cond(no)->4
cond(yes)->3
```



#### 1.4 Screenshots :

![](/home/kakul/Pictures/Screenshot from 2020-11-17 14-50-08.png)

​																	**Figure 1 : Results of PS1**															

### 2. Problem Statement 2

#### 2.1 Objective :

- create a preprocessor for assembler that will translate any 8085 assembly code into full capital letters and all numerals and remove the comments

#### 2.2 Algorithm and Implementation :

- Read the file 
- IF (Input sequence matches with format of comment) :
  - print nothing
- ELSE IF (Input sequence is a lowercase letter)
  - Convert it to uppercase (c-32) and print
- ELSE
  - print the input sequence

#### 2.3 Flowchart :

```flow
st=>start: Start
1=>operation: Read input sequence
cond=>condition: EOF reached ?
cond1=>condition: Input sequence matches 
with format of comment?
2=>operation: print nothing
cond2=>condition: Input sequence is 
a lowercase letter?
3=>operation: Convert it to uppercase (c-32) and print
4=>operation: print the input sequence
e=>end: end 
st->1->cond
cond(no)->cond1

cond(yes)->e
cond1(no)->cond2
cond1(yes)->2(left)->1
cond2(yes)->3(right)->1
cond2(no)->4(right)->1

```





#### 2.4 Screenshots :

![](/home/kakul/Pictures/Screenshot from 2020-11-17 17-14-22.png)

​															**Figure 2 : Results of PS2**

![](/home/kakul/Pictures/Screenshot from 2020-11-17 17-16-31.png)

​													**Figure 3 : Git log**





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
%{ 
 #include<stdio.h>

%}

%%
[;].* {fprintf(yyout, "");}

[a-z] {fprintf(yyout,"%c",yytext[0]-32);}

. {fprintf(yyout, "%s", yytext); }
%%

yywrap();

int main(int argc, char **argv)
{

	extern FILE *yyin, *yyout; 
  	yyin = fopen(argv[1], "r"); 
  	yyout = fopen(argv[2], "w"); 
	yylex();
	return 0;

}

```

### References

1. *Lex and Yacc: A Brisk Tutorial* , https://www2.cs.arizona.edu/~debray/Teaching/CSc453/DOCS/tutorial-large.pdf
2. _flex & bison_ , http://web.iitd.ac.in/~sumeet/flex__bison.pdf

