ui = input("Enter a string: ").upper()

#if ui[::-1].upper() == ui.upper():

if ui[::-1] == ui:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

#version 1
#ui = input("Enter a string: ")
#r = ui[::-1]
#if r == ui:
#    print("Its a palindrome")
#else:
#    print("Its not a palindrome")
    
    