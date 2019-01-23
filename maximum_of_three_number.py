# finding greatest of three number

def max3(a,b,c):
    if a > b and a > c:
            print('{} is Max'.format(a))
    elif b > c:
            print('{} is Max'.format(b))
    else:
        print('{} is Max'.format(b))



max3(9,6,1)
max3(9,60,1)
max3(9,6,10)
