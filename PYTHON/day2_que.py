#                18/06/2020

#Q:3) Check if a string is palindromeimport unittest

def str1(name):
    if(name[::]==name[::-1]):
        return ("palindrome")
    else:
        return ("not a palindrome")

#Q:4) 2X2 Matrix multiplication

def mul(X,Y):
    c=[[0,0],[0,0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
               c[i][j] += X[i][k] * Y[k][j]
    return c


#Q:5) 2X2 Matrix addition
def add1(X,Y):
    c=[[0,0],[0,0]]
    for i in range(len(X)):
        for j in range(len(X[0])):
            c[i][j] = X[i][j] + Y[i][j]

    return c


#Q:6) Display all the letters that occurs after the last vowel in a string	
#	 e.g., i/p: "string"
#	       o/p: "ng"
  

def word(str1):
    low=str1.lower()
    index=0
    c=0
    for i in low:
        index+=1
        if i in ['a','e','i','o','u']:
            c=index         
    return (low[c:])




