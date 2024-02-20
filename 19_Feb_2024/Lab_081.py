class Cal:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Cal()
result1 = object_ref.sum(3, 4)
result2 = object_ref.div(8, 4)
result3 = object_ref.sub(4, 5)
result4 = object_ref.mul(1, 0)
print(result1)
print(result2)
print(result3)
print(result4)
