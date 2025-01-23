import pygame
import random
pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hangman Game")

WHITE = (255, 255, 255)
ORANGE = (251, 140, 0)
RED = (213, 0, 0)
GREEN = (100, 221, 23)

background_image = pygame.image.load("board.jpg") 
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
menu_background_image = pygame.image.load("board.jpg") 
menu_background_image = pygame.transform.scale(menu_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

font = pygame.font.SysFont("Comic Sans MS", 30)
title_font = pygame.font.SysFont("Comic Sans MS", 50)
text_font = pygame.font.SysFont("Comic Sans MS", 18)

# Function to load words from a file (not used in Player vs Player mode)
def load_words():
    with open("words.txt", 'r') as f:
        words = f.read().split()
    return random.choice(words)

# Function to draw text on the window
def draw_text(text, font, color, x, y):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(x, y))
    window.blit(text_surf, text_rect)

# Function to draw hangman based on remaining attempts
def draw_hangman(remaining_attempts):
    base_x, base_y = 300, 450
    pygame.draw.line(window, WHITE, (base_x - 25, base_y + 50), (base_x - 25, base_y - 152), 5)
    pygame.draw.line(window, WHITE, (base_x - 25, base_y - 150), (base_x + 102, base_y - 150), 5)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 150), (base_x + 100, base_y - 105), 5) 
    pygame.draw.line(window, WHITE, (base_x - 100, base_y + 50), (base_x + 100, base_y + 50), 8)
    pygame.draw.line(window, WHITE, (base_x - 22, base_y + 20), (base_x + 15, base_y + 50), 5)
    if remaining_attempts <= 5:
        pygame.draw.circle(window, WHITE, (base_x + 100, base_y - 92), 15, 3)
    if remaining_attempts <= 4:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y - 40), (base_x + 100, base_y - 80), 3) 
    if remaining_attempts <= 3:
        pygame.draw.line(window, WHITE, (base_x + 70, base_y - 50), (base_x + 100, base_y - 70), 3) 
    if remaining_attempts <= 2:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y - 70), (base_x + 130, base_y - 50 ), 3) 
    if remaining_attempts <= 1:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y - 40), (base_x + 70, base_y + 5), 3) 
    if remaining_attempts <= 0:
        pygame.draw.line(window, WHITE, (base_x + 100, base_y), (base_x + 130, base_y + 65), 3)  
def player_vs_player():
    window.fill(WHITE)
    draw_text("Player 1, enter your word:", font, WHITE, WINDOW_WIDTH // 2, 100)
    pygame.display.update()
    word_entered = False
    player_word = ""

    while not word_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_word) > 0:
                        word_entered = True
                    else:
                        draw_text("Please enter a word!", font, RED, WINDOW_WIDTH // 2, 200)
                elif event.key == pygame.K_BACKSPACE:
                    player_word = player_word[:-1]
                elif event.key.isalpha() and len(player_word) < 15:  # limit word length
                    player_word += event.unicode.lower()

        draw_text("Word: " + player_word, font, WHITE, WINDOW_WIDTH // 2, 200)
        pygame.display.update()

    word_to_guess = player_word.lower()
    guessed_letters = set()
    remaining_attempts = 6
    guessed_word = ['_'] * len(word_to_guess)

    while remaining_attempts > 0 and '_' in guessed_word:
        window.blit(background_image, (0, 0))
        draw_hangman(remaining_attempts)
        draw_text("Word to guess: " + ' '.join(guessed_word), font, WHITE, WINDOW_WIDTH // 2, 100)
        draw_text("Letters already guessed: " + ', '.join(sorted(guessed_letters)), font, WHITE, WINDOW_WIDTH // 2, 150)
        draw_text(f"Remaining attempts: {remaining_attempts}", font, WHITE, WINDOW_WIDTH // 2, 200)
        pygame.display.update()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    letter = pygame.key.name(event.key).lower()
                    if letter.isalpha() and len(letter) == 1:
                        if letter in guessed_letters:
                            draw_text("You already guessed that letter!", font, RED, WINDOW_WIDTH // 2, 250)
                        else:
                            guessed_letters.add(letter)

                            if letter in word_to_guess:
                                for i in range(len(word_to_guess)):
                                    if word_to_guess[i] == letter:
                                        guessed_word[i] = letter
                            else:
                                remaining_attempts -= 1
                        waiting_for_input = False
        pygame.time.delay(300)  # delay to prevent too fast input

    window.blit(background_image, (0, 0))
    if '_' not in guessed_word:
        draw_text(f"Congratulations! The word was: {word_to_guess}", font, GREEN, WINDOW_WIDTH // 2, 100)
    else:
        draw_text(f"You lost! The word was: {word_to_guess}", font, RED, WINDOW_WIDTH // 2, 100)
    draw_text("Press 'Enter' to play again or 'Escape' to quit", font, WHITE, WINDOW_WIDTH // 2, 200)
    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_vs_player()  # Restart the game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Main Menu function
def main_menu():
    window.blit(menu_background_image, (0, 0)) 
    draw_text("Welcome to Hangman!", title_font, WHITE, WINDOW_WIDTH // 2, 100)
    draw_text("This is the rules of hangman:", text_font, WHITE, WINDOW_WIDTH // 2, 200)
    draw_text("You have to guess the word by inputting letters.", text_font, WHITE, WINDOW_WIDTH // 2, 220)
    draw_text("If you don't guess before running out of attempts, you lose.", text_font, WHITE, WINDOW_WIDTH // 2, 240)
    draw_text("So, are you ready to play?", text_font, WHITE, WINDOW_WIDTH // 2, 260)
    draw_text("1. Play Player vs Player", font, WHITE, WINDOW_WIDTH // 2, 330)
    draw_text("2. Exit", font, WHITE, WINDOW_WIDTH // 2, 380)
    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_vs_player()  # Start Player vs Player
                elif event.key == pygame.K_2:
                    pygame.quit()
                    exit()

# Start the game
main_menu()
