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
    with open("words.txt", 'r') as f:
        words = f.read().split()
    return random.choice(words)

def guess_word():
    guess_the_word = load_words()
    guess_letter = ['_'] * len(guess_the_word)
    use_letter = set() 
    remaining_attempt = 6 

    print("The word to guess have", len(guess_the_word), "letters.")
    
    while remaining_attempt > 0 and '_' in guess_letter:
        print("\nWord to guess :", ' '.join(guess_letter))
        print("Letters already use :", ', '.join(sorted(use_letter)))
        print(f"Remaining attempts : {remaining_attempt}")

        lettre = input("Submit a letter : ").lower()
        if lettre in use_letter:
            print("You submit this letter.")
            continue
        use_letter.add(lettre)
        if lettre in guess_the_word:
            print(f"Good job! The letter {lettre} is in the word.")
            for i in range(len(guess_the_word)):
                if guess_the_word[i] == lettre:
                    guess_letter[i] = lettre
        else:
            print(f"No you've making a mistake! The letter {lettre} isn't in the word.")
            remaining_attempt -= 1 

    if '_' not in guess_letter:
        print("\nWOOOW good job,",name, "the word was :", guess_the_word)
        return main_menu()
    else:
        print("\nNo you've lost",name, "the word was,",guess_the_word, "but you can try again .")
        return main_menu()

def main_menu():
    print ("Welcome to the Hangman Game!")
    print ("1. Play game")
    print ("2. Exit")
    choice = input("So what do you want to do ? ")
    os.system('cls')
    if choice == "1" : 
        print ("So ready to play",name,"good luck .")
        return guess_word()
    elif choice == "2" : 
        print ("Your already leaving ? See you later, for some more games", name, "!")
        time.sleep(3)
        os.system('cls')
        exit()
    else :
        print ("You have to choose a number between 1 and 3")
        return main_menu()
main_menu()