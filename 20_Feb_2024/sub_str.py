def find_substring(string, substring):
    if substring in string:
        index = string.index(substring)
        print("Substring found at index:", index)
    else:
        print("Substring not found")

string = "Hello, world!"
substring = "world"
find_substring(string, substring)