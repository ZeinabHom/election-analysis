import csv
import os
import random

choices=["P","S","R"]

customer_choice = input("please inter your choise?")

computer_choice = random.choice(choices)

if customer_choice == "P" and computer_choice == "p":
    print("OPSS!")

elif customer_choice == "P" and computer_choice == "R":
    print("congratulation!") 

else:
     print("oooppppppssss")


