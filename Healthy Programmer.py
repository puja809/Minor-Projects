"""
A programmer works from 9AM - 5 PM. We need to create a health reminder for him/her as below:

    1. Water Reminder  for every 30 min: Play a song after every 30 min till the user
       types "Drank Water". Once typed a log file will be generated with timestamp stating
       when the user drank water.

    2. Rest your Eyes reminder: After every 60 min A song will play to Meditate for 5 min. Once
    done type "Done" to generate the Log file

    3. Exercise Reminder: Every 45 min a song will play and remind you to do some movement and
    Log in the System
"""


import time
import pygame
# Starting the mixer
pygame.mixer.init()


# Setting the volume
pygame.mixer.music.set_volume(1)


# Function to get current time
def getdate():
    import datetime
    return datetime.datetime.now()


# Function for water reminder
def water_time():
    # Infinite Loop
    while True:
        time.sleep(1800)
        # Loading the song
        pygame.mixer.music.load("PaniPani.mp3")
        # Start playing the song
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(30)
        # print("Hi")
        n = input("Type Drank to stop the music and No to continue it: ")
        if n == "Drank":
            with open("DrinkWater-Log.txt", "a") as f:
                f.write("[" + str(getdate()) + "]" + ":  ")
                f.write(n + "\n")
            break
        else:
            pygame.mixer.music.play()


# Function for Meditation reminder
def meditate_reminder():
    # Infinite Loop
    while True:
        time.sleep(3600)
        # Loading the song
        pygame.mixer.music.load("Meditate.mp3")
        # Start playing the song
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(30)
        # print("Hi")
        n = input("Type Meditation Done to stop the music and No to continue it: ")
        if n == "Meditation Done":
            with open("Meditate-Log.txt", "a") as f:
                f.write("[" + str(getdate()) + "]" + ":  ")
                f.write(n + "\n")
            break
        else:
            pygame.mixer.music.play()


# Exercise Reminder function
def exercise_reminder():
    # Infinite Loop
    while True:
        time.sleep(2700)
        # Loading the song
        pygame.mixer.music.load("Dance.mp3")
        # Start playing the song
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(30)
        # print("Hi")
        n = input("Type Exercise Done to stop the music and No to continue it: ")
        if n == "Exercise Done":
            with open("Exercise-Log.txt", "a") as f:
                f.write("[" + str(getdate()) + "]" + ":  ")
                f.write(n + "\n")
            break
        else:
            pygame.mixer.music.play()


while True:
    if getdate().hour >= 17:
        print("Office Time Over!!")
        break
    else:
        print("Health Reminder Starts Now!!!!!")
        water_time()
        meditate_reminder()
        exercise_reminder()
