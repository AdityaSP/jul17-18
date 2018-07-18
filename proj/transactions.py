import core.bank

sa = core.bank.SA('Aditya')
print(sa.n, sa.b, sa.t)
sa.credit(100)
print(sa.n, sa.b, sa.t)

try:
    sa.debit(2000)
except core.bank.InsufficientBalanceError as err:
    print("Please check your balance and try again")
except Exception as err:
    print("Something went wrong. Contact the bank for details")

print(sa.n, sa.b, sa.t)
ca = core.bank.CA('ABC Ltd')
print(ca.n, ca.b, ca.t)
ca.credit(200)
print(ca.n, ca.b, ca.t)


# ac1 = core.bank.Account()
# print(type(ac1))

# ac1 = core.bank.Account('Aditya')
# print(ac1.n, ac1.b, ac1.t)
# ac1.credit(10000)
# print(ac1.n, ac1.b, ac1.t)
# ac1.debit(100)
# print(ac1.n, ac1.b, ac1.t)
#
# ac2 = core.bank.Account('John')
# print(ac2.n, ac2.b, ac2.t)
# ac2.credit(1000)
# print(ac2.n, ac2.b, ac2.t)