number = str(input("please input your credit card number with commas separating numbers"))
number = number.split()
print (number)


def lengthoflist():
    if len(number) > 16:
        print("this is too big, not valid")
    elif len(number) < 16:
        print("this is too small, not valid")
    else:
        print("correct!")

#
# def valuecheck():
#     try:
#         val = int(number)
#     except ValueError:
#         print("That's not an int!")









#    for i in range(0,number):
#        ele = str(input())
#        lst.append(ele)

#    if len(number) > 16:
#        print("this is not valid please retry")
#        quit()
#
lengthoflist()
# valuecheck()
