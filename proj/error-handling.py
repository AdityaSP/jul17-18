def f(n):
    nums = [1,2,3]
    print(nums[n])
    print(1/n)

try:
    f('df')
except ZeroDivisionError as err:
    print("Check the value of n: ", err)
except IndexError as err:
    print("Be in range please: ", err)
except Exception as err:
    print("Oops. Something went wrong. Was not expecting this")

# try:
#     f(5)
# except:
#     print("Something went wrong")
print("End of program")