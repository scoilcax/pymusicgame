# run in py.exe for clean interface / run in IDLE for better random selecting
# vars
from operator import itemgetter as grab
from re import split
from random import randrange as ran
from time import sleep
import os
auth=3
end=1
authcode="oli"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def convert(string):
    li = list(string.split(","))
    return li
def sd(text):
    try:
        e = float(text)
    except ValueError:
        e = text
    return e
def nums(text):
    # string integer sorting https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
    return [sd(c)for c in split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)',text)]
def pos(num,s):
    #Grab File And Sort
    leader = open("scores.csv").read().splitlines()
    leader = sorted(leader, reverse=True, key=nums)
    n = convert(leader[num-1])
    print(s, grab(1)(n), "Score:", grab(0)(n) )
def leaderboard():
    pos(2,"First")
    pos(3,"Second")
    pos(4,"Third")
    pos(5,"Fourth")
    pos(6,"Fifth")
    sleep(10)
#1. login/auth
while auth>0:
    authinput=input("Enter AuthCode: ")
    clear()
    if authcode==authinput:
        print("AuthCode accepted")
        sleep(1)
        auth=0
        end=1
        clear()
    elif ("top")==authinput:
        leaderboard()
    else:
        auth=auth-1
        print("Invalid AuthCode", auth, "Attempts Left")
        sleep(.5)
        end=0
if end==0:
    quit()
#2. import music list   
songs = open("songs.csv").read().splitlines()   
#3. run game
game=1
score=0
while game==1:
    # Rand Song
    song = convert(songs[ran(1,len(songs)-1)])
    #Print Artist and Initials
    print(grab(0)(song), " " , grab(2)(song))
    guesses=2
    # Guess
    while guesses>0:
        if input("Guess: ").upper()==grab(1)(song).upper():
            if guesses==2:
                point=3
            else:
                point=1
            score=score+point
            print("Correct", point, "points scored")
            guesses=0
        else:
            if guesses==1:
                game=0
            guesses=guesses-1
            print("Wrong answer", guesses, "guess Left")
            sleep(.5)            
#4. Score            
clear()
print("You scored", score, "points! \n Enter name to save: ")
score = str(score),",", str(input())
# Write Score To File
file = open("scores.csv", "a")
file.writelines("\n")
file.writelines(score)
file.close()
#5. Leader Board
leaderboard()
#Copyright Oli 2024

