# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:50:39 2023

@author: bryan
"""
import random

Namelist = ["Sophie", "Sylvia", "Phil", "Candice", "Mia", "Emma", "Amelia"]
name = random.choice(Namelist)

print(f"hello I am your AI girlfriend {name}")

Userinput = input()

def girlphase():
    Phrases =["Your are really cute", "you are hansome", 
              "we should meet up some time", "feel free to send me some money", 
              "is that a bananna in your pocket or are you just happy to see me", 
              "I think i like you", "Wow", "your hot", ]
    phase = random.choice(Phrases)
    print(phase)    

for i in range(7):
     Userinput = input()
     girlphase()



print("I would like to get to know you better")

Userinput = input()

print(" If you want the NSFW version cost just 12.95 a month bigboy")
