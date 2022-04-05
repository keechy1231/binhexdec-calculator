#Simple calculator

def dec_to_bin():
    dec_num = int(input("What number would you like to convert into binary?\n"))
    binary_num = bin(dec_num)
    print (binary_num)

def bin_to_dec():
    bin_num = input("What Binary number would you like to convert into decimal?(Please start your string with 0b)\n")
    decimal_num = int(bin_num, 2)
    print (decimal_num)

def hex_to_dec():
    hex_num = input("Please enter your Hex string to decode?(Please start your string with 0x)\n")
    decimal_num = int(hex_num, 0)
    print (decimal_num)

def dec_to_hex():
    dec_num = int(input("Please enter your number you would like to convert to Hex"))
    hex_num = hex(dec_num)
    print (hex_num)


choice = int(input ("What type of number would you like to convert? \nPress 1 for Decimal to Binary\nPress 2 for Binary to Decimal\nPress 3 for Hex to Decimal\nPress 4 for Decimal to Hex\n"))
if choice == 1:
    dec_to_bin()
elif choice == 2:
    bin_to_dec()
elif choice == 3:
    hex_to_dec()
elif choice == 4:
    dec_to_hex()
else:
    print("Please choose a valid option")
    