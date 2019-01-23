#___Prime Composite Check_________ 
def check(no):
    counter = 0 
    for i in range(1,int(no/2)):
     if(no%i == 0):
         counter = counter + 1
      
    if counter > 1:
         return "Composite"
    else:
         return "Prime"
#____________Max In List___________

def max_value():
    for i in range(1,11):
        print("--Upper--",i)
        for j in range(1,6):
            print("Lower",j)


#__________________________________



            
#____________Length Of List________

def list_length(list):
    return len(list)
#__________________________________





if __name__ == "__main__":
 list = [0,2,3,4,5,6,7,8,67,515]
 print(list_length(list))
 max_value()
# max_no(list)   
# x = check(17)
# print(x)
