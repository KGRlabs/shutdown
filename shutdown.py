from os import system
import time

answer = input("what is 5 + 5? ")

if str(answer) == 10:
    system("figlet that is the correct answer; you are a freaking genius!")
else:
    system("open cod-zombies.gif")
    time.sleep(2)
    system("figlet That is incorrect! you are dumb shutdown imminent!")
    system("shutdown 0")
