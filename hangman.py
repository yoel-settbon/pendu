import pygame
import random
pygame.init()

# Dimensions et configurations de la fenêtre
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

# Dictionnaire pour suivre les scores des joueurs
scores = {"Player 1": 0, "Player 2": 0}

def load_words():
    with open("words.txt", 'r') as f:
        words = f.read().split()
    return random.choice(words)

def draw_text(text, font, color, x, y):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(x, y))
    window.blit(text_surf, text_rect)

def draw_hangman(remaining_attempts):
    base_x, base_y = 300, 450
    pygame.draw.line(window, WHITE, (base_x - 25, base_y + 50), (base_x -25, base_y - 152), 5)
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

def display_scores():
    window.fill(WHITE)
    window.blit(background_image, (0, 0))
    draw_text("Scores", title_font, WHITE, WINDOW_WIDTH // 2, 50)
    draw_text(f"Player 1: {scores['Player 1']}", font, WHITE, WINDOW_WIDTH // 2, 150)
    draw_text(f"Player 2: {scores['Player 2']}", font, WHITE, WINDOW_WIDTH // 2, 200)
    draw_text("Click to return to the menu", font, WHITE, WINDOW_WIDTH // 2, 250)
    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Vérifier si le clic est un clic gauche
                    main_menu()

def player_vs_player():
    window.fill(WHITE)
    window.blit(background_image, (0, 0))
    draw_text("Player 1, enter your word:", font, WHITE, WINDOW_WIDTH // 2, 100)
    pygame.display.update()
    word_entered = False
    player_word = ""
    
    while not word_entered:
        window.fill(WHITE)
        window.blit(background_image, (0, 0))
        draw_text("Player 1, enter your word:", font, WHITE, WINDOW_WIDTH // 2, 100)
        draw_text("Word: " + player_word, font, WHITE, WINDOW_WIDTH // 2, 200)
        if len(player_word) == 0:
            draw_text("Please enter a word!", font, RED, WINDOW_WIDTH // 2, 250)       
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_word) > 0:
                        word_entered = True
                    else:
                        draw_text("Please enter a word!", font, RED, WINDOW_WIDTH // 2, 250)
                elif event.key == pygame.K_BACKSPACE:
                    player_word = player_word[:-1]
                elif 97 <= event.key <= 122 and len(player_word) < 15:
                    player_word += chr(event.key).lower()

    window.fill(WHITE)
    window.blit(background_image, (0, 0))
    draw_text("Player 2, guess the word!", font, WHITE, WINDOW_WIDTH // 2, 100)
    draw_text("Word: " + " ".join("_" * len(player_word)), font, WHITE, WINDOW_WIDTH // 2, 200)
    pygame.display.update()

    guessed_letters = set()
    word_to_guess = player_word
    guessed_word = ["_"] * len(word_to_guess)
    remaining_attempts = 6

    while remaining_attempts > 0 and "_" in guessed_word:
        window.fill(WHITE)
        window.blit(background_image, (0, 0))
        draw_hangman(remaining_attempts)
        draw_text("Player 2, guess the word!", font, WHITE, WINDOW_WIDTH // 2, 50)
        draw_text("Word: " + " ".join(guessed_word), font, WHITE, WINDOW_WIDTH // 2, 100)
        draw_text("Guessed letters: " + ", ".join(sorted(guessed_letters)), font, WHITE, WINDOW_WIDTH // 2, 150)
        draw_text(f"Remaining attempts: {remaining_attempts}", font, WHITE, WINDOW_WIDTH // 2, 200)
        pygame.display.update()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche de la souris
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Vous pouvez ajouter une logique pour cliquer sur une lettre si nécessaire
                    # Par exemple, vous pourriez afficher les lettres de l'alphabet sur l'écran
                    # et permettre de cliquer pour les deviner.
                    waiting_for_input = False
        pygame.display.update()

    window.fill(WHITE)
    window.blit(background_image, (0, 0))

    if "_" not in guessed_word:
        draw_text(f"Congratulations Player 2! The word was: {word_to_guess}", font, GREEN, WINDOW_WIDTH // 2, 100)
        scores["Player 2"] += 1  # Player 2 gagne
    else:
        draw_text(f"Sorry Player 2, you lost! The word was: {word_to_guess}", font, RED, WINDOW_WIDTH // 2, 100)

    draw_text("Click to play again or click to quit", font, WHITE, WINDOW_WIDTH // 2, 200)
    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche de la souris
                main_menu()
def guess_word():
    guess_the_word = load_words()
    guess_letter = ['_'] * len(guess_the_word)
    use_letter = set() 
    remaining_attempt = 6 
    while remaining_attempt > 0 and '_' in guess_letter:
        window.blit(background_image, (0, 0)) 
        draw_hangman(remaining_attempt)
        draw_text("The word to guess: " + ' '.join(guess_letter), font, WHITE, WINDOW_WIDTH // 2, 100)
        draw_text("Letters already used: " + ', '.join(sorted(use_letter)), font, WHITE, WINDOW_WIDTH // 2, 150)
        draw_text(f"Remaining attempts: {remaining_attempt}", font, WHITE, WINDOW_WIDTH // 2, 200)
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
    window.blit(background_image, (0, 0))  
    if '_' not in guess_letter:
        draw_text(f"Congratulations! The word was: {guess_the_word}", font, GREEN, WINDOW_WIDTH // 2, 100)
    else:
        draw_text(f"You lost! The word was: {guess_the_word}", font, RED, WINDOW_WIDTH // 2, 100)
    draw_text("Press 'Enter' to return to the menu or 'Escape' to quit", font, WHITE, WINDOW_WIDTH // 2, 200)
    pygame.display.update()
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
def main_menu():
    window.blit(menu_background_image, (0, 0))
    window.blit(menu_background_image, (0, 0)) 
    draw_text("Welcome to Hangman!", title_font, WHITE, WINDOW_WIDTH // 2, 50)
    draw_text("This is the rules of hangman :", text_font, WHITE, WINDOW_WIDTH // 2, 125)
    draw_text("You have to find the hiding word, for that you have to give letter .", text_font, WHITE, WINDOW_WIDTH // 2, 170)
    draw_text("If you didn't find the word before all your lives gone,", text_font, WHITE, WINDOW_WIDTH // 2, 195)
    draw_text("this is the end for you .", text_font, WHITE, WINDOW_WIDTH // 2, 220)
    draw_text("So ready to play ?", text_font, WHITE, WINDOW_WIDTH // 2, 245)
    draw_text("1. Play Game", font, WHITE, WINDOW_WIDTH // 2, 315)
    draw_text("2. Player vs Player", font, WHITE, WINDOW_WIDTH // 2, 365)
    draw_text("3. Show Scores", font, WHITE, WINDOW_WIDTH // 2, 415)
    draw_text("4. Exit", font, WHITE, WINDOW_WIDTH // 2, 465)
    draw_text("Game developers : Yoel, Manuel and Jerome .", text_font, WHITE, WINDOW_WIDTH// 4, 530)   
    pygame.display.update()
    waiting_for_input = True
    pygame.display.update()
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500:
                    if 300 <= mouse_y <= 340:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    elif 350 <= mouse_y <= 390:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    elif 400 <= mouse_y <= 440:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    elif 450 <= mouse_y <= 490:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500:
                    if 300 <= mouse_y <= 340:
                        guess_word()
                    elif 350 <= mouse_y <= 390:
                        player_vs_player()
                    elif 400 <= mouse_y <= 440:
                        display_scores()
                    elif 450 <= mouse_y <= 490:
                        exit()
main_menu()