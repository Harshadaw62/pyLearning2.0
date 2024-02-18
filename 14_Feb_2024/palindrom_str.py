def reverse_str(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


org_str = input("Enter string: ")
org_str=org_str.lower()
revs_str=reverse_str(org_str)
print(f"Reverse string is {revs_str}")

if org_str==revs_str:
    print("String is palindrome")
else:
    print("String is not palindrome")


