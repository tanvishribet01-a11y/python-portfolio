# Project 1 : Snake Water Gun Game
'''
 1 for snake
-1 for water
 0 for gun
 '''
import random

computer =random.choice([0,1,-1])
youstr =(input("enter yor choice (s/w/g):"))
youDict ={"s":1,"w":-1,"g":0}
you =youDict[youstr]

if(computer == you):
    print("Draw")

else:

     if(computer==-1 and you==1):
        print("You win!")

     elif(computer==-1 and you==0):
        print("You lost")

     elif(computer==1 and you==0):
        print("You win!")

     elif(computer==1 and you==-1):
        print("You lost")

     elif(computer==0 and you==-1):
        print("You win!")

     elif(computer==0 and you==1):
        print("You lost")

     else:
        print("something went wrong")





