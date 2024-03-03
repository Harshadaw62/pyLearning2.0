def check_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Check if the sorted strings are equal
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if check_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# -----------------------------------------------------

a = input("Enter string 1:")
b = input("Enter string 2:")
count = 0
for i in a:
    for j in b:
        if i == j:
            count = count + 1
if count == len(a):
    print("Strings are anagram of each other.")
else:
    print("Strings are not anagram of each other.")
