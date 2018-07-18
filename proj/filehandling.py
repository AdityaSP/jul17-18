#context managers
with open('trial.txt') as fh:
    s = fh.read()
    print(type(s))
    print("READ:", s)

print("End of program")

# fh = open('trial.txt', 'rt')
# s = fh.read()
# print(type(s))
# print("READ:", s)
# fh.close()



#fh = open('log\\trial.txt', 'w')
#fh = open('log/trial.txt', 'w')
#fh = open(r'log\trial.txt', 'w')
# fh = open(r'E:\backup\python software\trial.txt', 'w')
# fh.write('line 1')
# fh.write('\nline 2')
# fh.close()

# fh = open('trial.txt', 'at')
# fh.write('\nline 3')
# fh.write('\nline 4')
# fh.close()


# fh = open('trial.txt', 'rt')
# s = fh.read()
# print(type(s))
# print("READ:", s)
#
# s = fh.read()
# print("READ:", s)
#
# fh.seek(0)
# s = fh.read()
# print("READ:", s)
#
# fh.seek(0)
# l = fh.readlines()
# print(type(l))
# print("LINES:", l)
# print("--------------")
# fh.seek(0)
# for line in fh:
#     print(line)
#
# fh.close()