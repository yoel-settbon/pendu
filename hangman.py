import pygame
import os
import time
from random import choice

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
    