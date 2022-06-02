"""
A soldier function will take 3 parameters:
    1. Path of the folder to rename the files(not folders)
    2. File not to change
    3. Extension for which the files will be numbered from 1 to n
"""

import os


def gen(n1):
    for i in range(1, n1, 1):
        yield i


rng = int(input("Enter the Range up to which you want to number the files: "))
n = gen(rng)


def soldier(path, file, extension):
    os.chdir(path)
    lst = os.listdir(path)
    for i in range(0, len(lst), 1):
        if lst[i] != file and os.path.isfile(lst[i]) is True:
            os.rename(lst[i], lst[i].capitalize())
        if os.path.isfile(lst[i]) is True:
            ls = lst[i].split(".")
            if ls[1] == extension:
                os.rename(f"{ls[0]}.{ls[1]}", f"{str(n.__next__())}.{ls[1]}")

    pass


soldier("D:\\test", "puja - Copy (13).txt", "docx")
print("Soldier has prettified your folder!!")
