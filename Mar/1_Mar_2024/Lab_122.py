path = "C:/Users/ThinkPad/PycharmProjects/pyLearning2X/Feb/feb.txt"
with open(path) as file:
    print(file.read())

print("------------")
import os

print(os.getcwd())