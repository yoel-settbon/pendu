import pygame
import os
import random
import time
from random import choice

print ("So who's the one who's going to play ?")
name = input("Player, what's your name ? ""\n")
print ("Nice to meet you, " + name + " ! Are you ready to play the hangman game ?")
time.sleep(2)
print ("Loading...")
time.sleep(0.5)
rules = open("rules.txt")
rule = rules.read()
print (rule)
time.sleep(5)

def load_words():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words

def main_menu():
    print ("Welcome to the Hangman Game!")
    print ("1. Player vs Computer")
    print ("2. Player vs Player")
    print ("3. Exit")
    choice = input("So what do you want to do ? ")
    os.system('cls')
    if choice == "3" : 
        print ("Your already leaving ? See you later, for some more games !")
        time.sleep(3)
        os.system('cls')
        exit()
    else :
        print ("you have to choose a number between 1 and 3")
        return main_menu()
main_menu()