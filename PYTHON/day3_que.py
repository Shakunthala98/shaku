'''
Q:7) Sort the similar anagrams in a list. 
	i/p: list = ["eat", "tea", "far", "raf", "arf"]
	o/p: [["eat","tea"], ["far", "raf", "arf"]]
'''	
def groupAnagrams(strs):
      result = {}
      for i in strs:
         x = "".join(sorted(i))
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())

'''	
Q:8) Display the length of longest string which is in alphabetical order 
	i/p: str = "abcaklmoeeffd" 
	o/p: 5 (aklmo)
'''
def alph(s):
    tmp=''
    res=''
    for i in range(len(s)):
        tmp += s[i]
        if len(tmp) > len(res):
            res = tmp
        if i > len(s)-2:
            break
        if s[i] > s[i+1]:
            tmp = ''
    return ("Longest substring in alphabetical order is: {}".format(res))

'''
Q:9) Take a number input from the user, convert it into binary and count the occurence of that binary number number in 100110110
	i/p: 5 (decimal equivalent to 5 is 101)
	o/p: 1 (101 occurs only once in 100110110)
'''
def binary(num):
    bin1=format(num,'b')
    a="100110110"
    return bin1+" "+ str(a.count(bin1))

'''
Q:10) Return the string with the count of vowels occuring in it in ascending order. 
	e.g,  i/p:	str = "I am reading a book" 
		  o/p:  str = "reading book I am a" (reading - 3, book - 2, I - 1, am - 1, a - 1)
'''
def vow(str1):
    dict1={}
    count=0
    str1=str1.split()
    for i in str1:
        for j in i:
            if j in 'aeiouAEIOU':
                count+=1
                if i not in dict1.values():
                    dict1[count]=i
    return sorted(dict1.values(),reverse=True)


'''
Q:11) Perform matrix multiplication on 3X3 matrix and print the output matrix spirally

	e.g., 1 2 3    should be displayed as     1 2 3
		  4 5 6  ------------------------->   6 9 8
		  7 8 9                               7 4 5
'''
def mat(m1):
  str1=""
  a=len(m1)//2
  for i in range(0,a):
    for j in range(0,len(m1)):
      str1+=str(m1[i][j])
  for i in range(a,len(m1)):
    for j in range(-1,a):
      str1+=str(m1[i][j])
  return str1


'''
Q:12) Display the maximum length of substring which is palindrome 
	  eg., i/p: str = "cabbage"
		   o/p: 4 (abba)
'''          
def longpal(string): 
    maxLength = 1
    start = 0
    length = len(string) 
    low = 0
    high = 0
    for i in range(1, length): 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
    #print ("Longest palindrome substring is: ",end='') 
    return (string[start:start + maxLength]) 


  