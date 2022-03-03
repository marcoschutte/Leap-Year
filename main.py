year = int(input("Which year do you want to check? "))

flag = True

if(year % 4 == 0):
    flag = True
    if(year % 100 == 0):
        flag = False
        if(year % 400 == 0):
            flag = True
else:
    flag = False
    
if(flag == True):
    print("Leap year.")
elif(flag == False):
    print("Not leap year.")