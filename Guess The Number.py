"""We have a hidden number in the code and the user needs to guess it. But wait!! we have some
limitations:
1.Limited number of guesses are there that is 5
2.Once the guesses are over the Gave is also over
3. If the user guess the correct number, give him a shout-out and print the
number of guesses he took
4.Every time the user enters a number, display the number of guess left and whether the
number is greater or lesser than the original number
"""

"""                                     Guess The Number                                           """

n=67
i=0
while(True):
    print("Guess the number:")
    num=int(input())
    i=i+1
    if num>n and i<5:
        print("You have entered a number greater than original number")
        print("You have "+str(5-i)+" guess left")
    elif num<n and i<5:
        print("You have entered a number lesser than original number")
        print("You have " +str(5-i) + " guess left")
    elif num==n and i<5:
        print("Great!! You have guessed the correct number\n")
        print("You guessed the number in "+str(i)+" guesses")
        break
    if i==5 and num==n:
        print("Great!! You have guessed the correct number\n")
        print("You guessed the number in " + str(i) + " guesses")
    elif i==5 and num!=n:
        print("Sorry!! No More Guess left. Game is Over!!")
        break
