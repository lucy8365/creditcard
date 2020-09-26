def checkCard():
    number = str(input("please input your credit card number"))
    number = number.split()
    return number
    lengthoflist()

def lengthoflist():
    if len(number) > 16:
        print("this is too big, not valid")
    elif len(number) < 16:
        print("this is too small, not valid")
    else:
        print("correct!")










#    for i in range(0,number):
#        ele = str(input())
#        lst.append(ele)

#    if len(number) > 16:
#        print("this is not valid please retry")
#        quit()

checkCard()
print(number)
