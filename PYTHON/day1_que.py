#Q:1) Swapcase the string without using any inbuilt function. 
#	 i/p: str1 = "aBcDEFz"
#	 o/p: AbCdefZ
def strpalindrome(name):
    return (name.swapcase())
           



#========================================================
#Q:2)Display the sum of all the numbers in the given list -
#	 i/p: list1 = [[1,2,3],4,[5,6]]
#	 o/p: sum = 21
def listsum(lst):
    sum=0
    for i in lst:
        if(type(i)==int):
            sum=sum+(i)
        else:
            for j in i:
                sum=sum+(j)
    return sum


     
