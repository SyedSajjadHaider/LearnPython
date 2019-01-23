

#--------------------------
def reverse1(str1):
 return str1[::-1]
#---------------------- 

def reverse2(s):
    str = ""
    for char in s:
        str = char + str
    print(str)
    
#-----------------------
def length(str1):
 count = 0
 for c in str1:
        count = count + 1
 return count
#-----------------------


#-----------------------
string = 'sajjad'
result = string[::-1]
#----------------------

#reverse1(string)
#reverse2("syed")
length("syed")
