try:
    with open("TestData2.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfr:
    print("-----")
    print(fnfr)
finally:
    file.close()

