"""                  Health Management System

1. Take the name of Client as Input and create two files for each client:
    one for Diet and one of exercise

2. Ask the whether he/she wants to retrieve or log, diet or exercise files and act accordingly
"""


name = input("Enter the name of the client ")

try:
    f = open(name+"-Diet", "x")
    f.close()
    f = open(name+"-Exercise", "x")
    f.close()
except Exception as error:
    print(error)


def getdate():
    import datetime
    return datetime.datetime.now()


log = input("Do you want to Log or Retrieve the files: Log/Retrieve: ")
files = input("Which file you want to open: Diet/Exercise ")

if log == 'Log' and files == 'Diet':
    diet = input("Please Enter Your Diet: ")
    with open(name+"-Diet", "a") as f:
        f.write("["+str(getdate())+"]"+":  ")
        f.write(diet+"\n")
    print("You have successfully Logged the Diet!!")
elif log == 'Log' and files == 'Exercise':
    exercise = input("Please Enter Your Exercise: ")
    with open(name+"-Exercise", "a") as f:
        f.write("[" + str(getdate()) + "]" + ":  ")
        f.write(exercise+"\n")
    print("You have successfully Logged the Exercise!!")
elif log == 'Retrieve' and files == "Diet":
    with open(name+"-Diet", "rt") as f:
        print(f.read())
elif log == 'Retrieve' and files == "Exercise":
    with open(name+"-Exercise", "rt") as f:
        print(f.read())
