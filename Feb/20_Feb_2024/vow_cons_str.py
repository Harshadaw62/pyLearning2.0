def count_vowels_cons(string):
    vowels = 'aeiou'
    counts = {'vowels': 0, 'consonants': 0}

    for char in string:
        if char.lower() in vowels:
            counts['vowels'] += 1
        elif char.isalpha():
            counts['consonants'] += 1

    return counts


# Example usage:
inp_str = input("Enter the string: ")
result = count_vowels_cons(inp_str)
print("Vowel count:", result['vowels'])
print("Consonant count:", result['consonants'])

print("--------------------------------------------------------------------------")
vcount = 0
ccount = 0
str = input("Enter the string to check vowels and consonants: ")

# Converting entire string to lower case to reduce the comparisons
str1 = str.lower()
for i in range(0, len(str1)):
    # Checks whether a character is a vowel
    if str1[i] in ('a', "e", "i", "o", "u"):
        vcount = vcount + 1
    elif (str1[i] >= 'a' and str1[i] <= 'z'):
        ccount = ccount + 1
print(f"Total number of vowel are {vcount} \n consonant are {ccount}")

