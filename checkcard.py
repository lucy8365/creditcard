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
    everySecond = lst[1::2]
    otherValues = lst[::2]
    print(everySecond)
    print(otherValues)
    validate()

# take every seocn number 1,3,5 then do the same starting from second last then take another variable frm remianed multiples, adders fro every number in the list you multplu it by two
# check if theyare double digits if they ar then you split then you should have abig list , then you add them all up then add all the adders, then you %done if its 0 then true else not
# if number.isdigit():
#     print("good, these are integers")
# else:
#     print("ERROR MESSAGE")
# number = number.split(", ")
# print(number)


getNumber()
