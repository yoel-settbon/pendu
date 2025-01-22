import pygame
import random
import os
import time

# Initialize pygame
pygame.init()

# Set up window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load images
background_image = pygame.image.load("board.jpg")  # Replace with your in-game background image
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Load the menu background image
menu_background_image = pygame.image.load("board.jpg")  # Replace with your menu background image
menu_background_image = pygame.transform.scale(menu_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Font settings
font = pygame.font.SysFont("Comic Sans MS", 30)
title_font = pygame.font.SysFont("Comic Sans MS", 50)

# Load words from the file
def load_words():
    with open("words.txt", 'r') as f:
        words = f.read().split()
    return random.choice(words)

# Draw text function
def draw_text(text, font, color, x, y):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(x, y))
    window.blit(text_surf, text_rect)

# Draw the hangman according to the number of attempts left
def draw_hangman(remaining_attempts):
    base_x, base_y = 300, 500
    pygame.draw.line(window, WHITE, (base_x, base_y), (base_x, base_y - 152), 5)  # The pole
    pygame.draw.line(window, WHITE, (base_x, base_y - 150), (base_x + 102, base_y - 150), 5)  # The top bar
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 150), (base_x + 100, base_y - 100), 5)  # The rope

    if remaining_attempts <= 5:
        pygame.draw.circle(window, WHITE, (base_x + 100, base_y - 60), 20, 5)  # Head
    if remaining_attempts <= 4:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y - 40), (base_x + 100, base_y), 5)  # Body
    if remaining_attempts <= 3:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y - 20), (base_x + 70, base_y), 5)  # Left arm
    if remaining_attempts <= 2:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y - 20), (base_x + 130, base_y), 5)  # Right arm
    if remaining_attempts <= 1:
        pygame.draw.line(window, RED, (base_x + 100, base_y), (base_x + 70, base_y + 40), 5)  # Left leg
    if remaining_attempts <= 0:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y), (base_x + 130, base_y + 40), 5)  # Right leg

# Game function
def guess_word():
    guess_the_word = load_words()
    guess_letter = ['_'] * len(guess_the_word)
    use_letter = set() 
    remaining_attempt = 6 

    # Game loop
    while remaining_attempt > 0 and '_' in guess_letter:
        window.blit(background_image, (0, 0))  # Draw background

        # Draw hangman
        draw_hangman(remaining_attempt)

        # Display game status
        draw_text("The word to guess: " + ' '.join(guess_letter), font, WHITE, WINDOW_WIDTH // 2, 100)
        draw_text("Letters already used: " + ', '.join(sorted(use_letter)), font, WHITE, WINDOW_WIDTH // 2, 150)
        draw_text(f"Remaining attempts: {remaining_attempt}", font, WHITE, WINDOW_WIDTH // 2, 200)

        pygame.display.update()

        # Event handling (waiting for a letter guess)
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    letter = pygame.key.name(event.key).lower()

                    # Only accept single alphabetic letters
                    if letter.isalpha() and len(letter) == 1:
                        if letter in use_letter:
                            print("You already guessed that letter!")
                        else:
                            use_letter.add(letter)

                            if letter in guess_the_word:
                                for i in range(len(guess_the_word)):
                                    if guess_the_word[i] == letter:
                                        guess_letter[i] = letter
                            else:
                                remaining_attempt -= 1
                        waiting_for_input = False

    # End of game
    window.blit(background_image, (0, 0))  # Draw background
    if '_' not in guess_letter:
        draw_text(f"Congratulations! The word was: {guess_the_word}", font, GREEN, WINDOW_WIDTH // 2, 100)
    else:
        draw_text(f"You lost! The word was: {guess_the_word}", font, RED, WINDOW_WIDTH // 2, 100)

    draw_text("Press 'Enter' to play again or 'Escape' to quit", font, WHITE, WINDOW_WIDTH // 2, 200)
    pygame.display.update()

    # Wait for the user to press a key to restart or quit
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    guess_word()  # Restart the game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Main menu function
def main_menu():
    window.blit(menu_background_image, (0, 0))  # Draw the menu background image
    draw_text("Welcome to Hangman!", title_font, WHITE, WINDOW_WIDTH // 2, 100)
    draw_text("1. Play Game", font, WHITE, WINDOW_WIDTH // 2, 200)
    draw_text("2. Exit", font, WHITE, WINDOW_WIDTH // 2, 250)
    
    pygame.display.update()

    # Handle main menu choice
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    guess_word()  # Start the game
                elif event.key == pygame.K_2:
                    pygame.quit()
                    exit()

# Run the game
main_menu()
