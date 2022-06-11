#Simple calculator
import time

binary_num = []
decimal_num = []
hex_num = []


print("Binhexdec Calc Version 1.0\n\n\n")

def dec_to_bin():
    dec_num = int(input("What number would you like to convert into binary?\n\n"))
    binary_num.append(bin(dec_num))
    print("\n")
    print("Your Binary number(s) are:", binary_num)
    time.sleep(0.6)

def bin_to_dec():
    bin_num = input("What Binary number would you like to convert into decimal?(Please start your string with 0b)\n\n")
    decimal_num.append(int(bin_num, 2))
    pring("\n")
    print ("Your Decinal number(s) are:", decimal_num)
    time.sleep(0.6)

def hex_to_dec():
    hex_num = input("Please enter your Hex string to decode?(Please start your string with 0x)\n\n")
    decimal_num.append(hex_num, 0)
    print("\n")
    print ("Your Decimal number(s) are:", decimal_num)
    tim.sleep(0.6)

def dec_to_hex():
    dec_num = int(input("Please enter your number you would like to convert to Hex\n\n"))
    hex_num.append(hex(dec_num))
    print("\n")
    print ("Your Hexidecimal number(s) are:", hex_num)
    time.sleep(0.6)


choice = int(input ("What type of number would you like to convert? \nPress 1 for Decimal to Binary\nPress 2 for Binary to Decimal\nPress 3 for Hex to Decimal\nPress 4 for Decimal to Hex\n\n"))
while choice == 1:
    dec_to_bin()
    choice = int(input("\nDo you want to convert another number to binary?\nPress 1 for yes: \nPress 2 for no and to exit\n\n"))

while choice == 2:
    bin_to_dec()
    choice = int(input("\nDo you want to convert another Binary number to Decimal2?\nPress 2 for yes: \nPress 3 for no and to exit\n\n"))

while choice == 3:
    hex_to_dec()
    choice = int(input("\nDo you want to convert another Hex number to Decimal?\nPress 3 for yes: \nPress 4 for no and to exit\n\n"))

while choice == 4:
    dec_to_hex()
    choice = int(input("\nDo you want to convert another number to Hex?\nPress 4 for yes: \nPress 5 for no and to exit\n\n"))

while choice != 1 or 2 or 3 or 4:
    choice = int(input("\nPlease choose a valid option\n\n"))
