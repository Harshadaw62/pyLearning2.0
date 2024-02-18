def reverse_str(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


name = input("Enter the string u want to reverse: ")
# print(reverse_str(name))   This is also possible
name1 = reverse_str(name)
print(name1)

