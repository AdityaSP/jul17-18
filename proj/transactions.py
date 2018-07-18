import core.bank
# ac1 = core.bank.Account()
# print(type(ac1))

ac1 = core.bank.Account('Aditya')
print(ac1.n, ac1.b, ac1.t)
ac1.credit(10000)
print(ac1.n, ac1.b, ac1.t)
ac1.debit(100)
print(ac1.n, ac1.b, ac1.t)

ac2 = core.bank.Account('John')
print(ac2.n, ac2.b, ac2.t)
ac2.credit(1000)
print(ac2.n, ac2.b, ac2.t)