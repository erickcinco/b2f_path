import os

while True:
    path = input("Enter windows path: ")
    print("Linux path: {}".format(path.replace('\\', '/')))