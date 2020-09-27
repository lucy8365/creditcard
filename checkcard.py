def menu():
    choice = input('''
welcome to the user menu please select an
option from 1 - 4
1- check my card
2 - import numbers to check
3 - generate a valid CC number
4 - QUIT''')
    if choice == 1 :
        print("you chose check my card")
        getNumber()
    elif choice == 2 :
        print("you chose to import numbers to check")
        importnumbers()
    elif choice == 3:
        print("you chose to generate a valid cc nummber")
        ccnumber()
    elif choice == 4:
        print("you chose quit")
        quit()

lst = []
def getNumber():
    for i in range(16):
        f = input("enter digit on credit card")
        lst.append(f)
        print(lst)
    seperatesecond()
    return lst


def seperatesecond():
    everySecond = []
    everySecond = lst[1::2]
    otherValues = lst[::2]
    my_new_list = [i * 2 for i in everySecond]
    sum_of_digits = sum(my_new_list)
    sum_of_odd = sum(otherValues)
    newvalue = (sum_of_digits+sum_of_odd)
    print(sum_of_digits)
    print(sum_of_odd)
    print(newvalue)
    if newvalue % 10 == 0:
        print("this is valid")
    else:
        print("NOT VALID")

    # print(everySecond)
    # print(otherValues)
    # return everySecond
    # return otherValues






# take every seocn number 1,3,5 then do the same starting from second last then
# take another variable frm remianed multiples, adders fro every number in the list you multplu it by two
# check if theyare double digits if they ar then you split then you should have
#abig list , then you add them all up then add all the adders, then you %done if its 0 then true else not


# if number.isdigit():
#     print("good, these are integers")
# else:
#     print("ERROR MESSAGE")
# number = number.split(", ")
# print(number)


# def validate():
#     doublesecond = for x in everySecond
# def validate():
#     creditcard = creditcard[::-1]
#     creditcard = [int(x) for x in creditcard]
#     doubleSecondDigit = list()
#     digits = list(enumerate(creditcard,start=1))
#     for index, digit in digits:
#         if index % 2 == 0:
#             doubleSecondDigit.append(digit*2)
#         else:
#             doubleSecondDigit.append(digit)
#
#     doubleSecondDigit = [sum_digits(x) for x in doubleSecondDigit]
#     # sum all digits
#     sum_of_digits = sum(doubleSecondDigit)
#     # return True or False
#     return sum_of_digits % 10 == 0
#
# if __name__ == "__main__":
#     print(validate(getNumber()))
#
#

getNumber()
