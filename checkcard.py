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
        importNumbers()
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
    validate()
    return lst


def validate():
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
        menu()
    else:
        print("NOT VALID")
        quit()
    return newvalue


def importNumbers():
    # infile = open("MWDCredit.txt","r")
    # # initialize num here
    # num = cc = (infile.readline().strip())
    # print(format("Card Number", "20s"), ("Valid / Invalid"))
    # print("------------------------------------")
    # while cc!= "EXIT":
    #     everySecond = []
    #     everySecond = num[1::2]
    #     otherValues = num[::2]
    #     my_new_list = [i * 2 for i in everySecond]
    #     sum_of_digits = sum(my_new_list)
    #     sum_of_odd = sum(otherValues)
    #     newvalue = (sum_of_digits+sum_of_odd)
    #     print(sum_of_digits)
    #     print(sum_of_odd)
    #     print(newvalue)
    #     if newvalue % 10 == 0:
    #         print("this is valid")
    #         menu()
    #     else:
    #         print("NOT VALID")
    #         quit()
    #     return newvalue

    # read = open("MWDCredit.txt", 'r')
    # i = 0
    # for line in read:
    #     print(line)
    # read.close()
    # inputNumbers = line.append()
    # print(inputNumbers)

# if number.isdigit():
#     print("good, these are integers")
# else:
#     print("ERROR MESSAGE")
# number = number.split(", ")
# print(number)


menu()
