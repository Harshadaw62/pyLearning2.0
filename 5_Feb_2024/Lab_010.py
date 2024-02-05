name = "Harshada"

print(len(name))  # len start with 1
print(name[4])  # print char stored at index 4
print(name[5])  # Index start with 0
# print(name[6]) # IndexError: string index out of range
print(len(name) - 1)  # printlength of string name-1
print(name[len(name) - 1]) #frst print length of string name-1 and then print char stored at name[]

# String - Immutability
# that can't be changed, modify
string = "Hello"
string = "Pramod"
print(string)
#we can change whole string but cant change single char of string
# string[0] = "P" #TypeError: 'str' object does not support item assignment
