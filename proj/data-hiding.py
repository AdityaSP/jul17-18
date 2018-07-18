#name mangling
class Shape():
    def __init__(self, n):
        self.__name = n
    def get_name(self):
        return self.__name
    def set_name(self, v):
        raise NameError("Cannot change the value of name once created")

sq = Shape('Square')
print(sq.get_name())
#sq.set_name('Circle')

print(dir(sq))
print(sq._Shape__name)
sq._Shape__name = 'Circle'
print(sq._Shape__name)


# class Shape():
#     def __init__(self, n):
#         self.__name = n
#
# sq = Shape('Square')
# print(sq.__name)
# sq.__name = 'Circle'
# print(sq.__name)

# class Shape():
#     def __init__(self, n):
#         self.name = n
#
# sq = Shape('Square')
# print(sq.name)
# sq.name = 'Circle'
# print(sq.name)
#
