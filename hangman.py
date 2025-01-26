import pygame       # import a graphical interface
import random       # import to pick a random word in words.txt

# import all the pygame module
pygame.init()
losing_sound = pygame.mixer.Sound('audio\losing-sound.wav')
victory_sound = pygame.mixer.Sound('audio/victory-sound.wav')
pygame.mixer.music.set_volume(0.5)

# defined the size of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# title of the game 
pygame.display.set_caption("Hangman Game")

# defined all the colors we going to use
WHITE = (255, 255, 255)
RED = (213, 0, 0)
GREEN = (100, 221, 23)
ORANGE = (255, 138, 51)

# defined the the background image and the size in game window
background_image = pygame.image.load("board.jpg") 
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# defined all the writing we going tu use
font = pygame.font.SysFont("Comic Sans MS", 30)
title_font = pygame.font.SysFont("Comic Sans MS", 50)
text_font = pygame.font.SysFont("Comic Sans MS", 18)

scores = {"Player 1": 0, "Player 2": 0}

# defined functions for diferent musics during the game
def play_menu_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('audio\menu_music.wav')
    pygame.mixer.music.play(-1) 

def play_game_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('audio\game-music.wav')
    pygame.mixer.music.play(-1)

def play_scores_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('audio\scores-music.wav')
    pygame.mixer.music.play(-1)

def load_words():
    # function to pick a random word in the file txt
    with open("words.txt", 'r') as f:
        words = f.read().split()
    return random.choice(words)

def draw_text(text, font, color, x, y):
    # function to write in graphical interface
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(x, y))
    window.blit(text_surf, text_rect)

def draw_hangman(remaining_attempts):
    # function to draw and defined the hangman place
    base_x, base_y = 350, 500

    pygame.draw.line(window, WHITE, (base_x - 25, base_y + 50), (base_x -25, base_y - 152), 5)
    pygame.draw.line(window, WHITE, (base_x - 25, base_y - 150), (base_x + 102, base_y - 150), 5)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 150), (base_x + 100, base_y - 105), 5) 
    pygame.draw.line(window, WHITE, (base_x - 100, base_y + 50), (base_x + 100, base_y + 50), 8)
    pygame.draw.line(window, WHITE, (base_x - 22, base_y + 20), (base_x + 15, base_y + 50), 5)

    # draw a part of hangman body to every false letter
    if remaining_attempts <= 5:
        pygame.draw.circle(window, GREEN, (base_x + 100, base_y - 92), 15, 3)
    if remaining_attempts <= 4:
        pygame.draw.line(window, GREEN, (base_x + 100, base_y - 40), (base_x + 100, base_y - 80), 3) 
    if remaining_attempts <= 3:
        pygame.draw.line(window, ORANGE, (base_x + 70, base_y - 50), (base_x + 100, base_y - 70), 3) 
    if remaining_attempts <= 2:
        pygame.draw.line(window, ORANGE, (base_x + 100, base_y - 70), (base_x + 130, base_y - 50 ), 3) 
    if remaining_attempts <= 1:
        pygame.draw.line(window, RED, (base_x + 100, base_y - 40), (base_x + 70, base_y + 5), 3) 
    if remaining_attempts <= 0:
        pygame.draw.line(window, RED, (base_x + 100, base_y), (base_x + 130, base_y + 65), 3)

def lose() :
    # draw the entire hangman after you lose
    base_x, base_y = 350, 500

    pygame.draw.line(window, WHITE, (base_x - 25, base_y + 50), (base_x -25, base_y - 152), 5)
    pygame.draw.line(window, WHITE, (base_x - 25, base_y - 150), (base_x + 102, base_y - 150), 5)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 150), (base_x + 100, base_y - 105), 5) 
    pygame.draw.line(window, WHITE, (base_x - 100, base_y + 50), (base_x + 100, base_y + 50), 8)
    pygame.draw.line(window, WHITE, (base_x - 22, base_y + 20), (base_x + 15, base_y + 50), 5)
    pygame.draw.circle(window, WHITE, (base_x + 100, base_y - 92), 15, 3)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 40), (base_x + 100, base_y - 80), 3)
    pygame.draw.line(window, WHITE, (base_x + 70, base_y - 50), (base_x + 100, base_y - 70), 3)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 70), (base_x + 130, base_y - 50 ), 3)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 40), (base_x + 70, base_y + 5), 3)
    pygame.draw.line(window, WHITE, (base_x + 100, base_y - 40), (base_x + 130, base_y + 5), 3) 

def display_scores():  
    # function to see score in player vs player mode
    play_scores_music()
    window.blit(background_image, (0, 0))

    draw_text("Scores", title_font, WHITE, WINDOW_WIDTH // 2, 50)
    draw_text(f"Player 1: {scores['Player 1']}", font, WHITE, WINDOW_WIDTH // 2, 150)
    draw_text(f"Player 2: {scores['Player 2']}", font, WHITE, WINDOW_WIDTH // 2, 200)
    draw_text("Press ENTER to go back to the menu", font, WHITE, WINDOW_WIDTH // 2, 250)
    draw_text("Press SPACE to play a game", font, WHITE, WINDOW_WIDTH // 2, 300)
    draw_text("Press ECHAP to quit the game", font, WHITE, WINDOW_WIDTH // 2, 350)
    
    # update the content of the window in graphical interface
    pygame.display.update()

    # different input to nagated in all the game menu
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()
                elif event.key == pygame.K_SPACE:
                    player_vs_player()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


def player_vs_player():
    # function to defined the game mode player vs player

    window.blit(background_image, (0, 0))
    
    draw_text("Player 1, enter your word:", font, WHITE, WINDOW_WIDTH // 2, 100)
    
    pygame.display.update()

    word_entered = False
    player_word = "" 

    while not word_entered:
        # ask player 1 to pick a word
        window.blit(background_image, (0, 0))
        draw_text("Player 1, enter your word:", font, WHITE, WINDOW_WIDTH // 2, 100)
        draw_text("Word: " + player_word, font, WHITE, WINDOW_WIDTH // 2, 200)
        if len(player_word) == 0:
            draw_text("Please enter a word!", font, RED, WINDOW_WIDTH // 2, 250) 

        pygame.display.update() 
              
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_word) > 0:
                        word_entered = True
                    else:
                        draw_text("Now you can write the word you want.", font, RED, WINDOW_WIDTH // 2, 250)
                elif event.key == pygame.K_BACKSPACE:
                    player_word = player_word[:-1]
                    # possibility to delete letter if you'd make a mistake

                elif 97 <= event.key <= 122 and len(player_word) < 15:
                    # selecte all the letter on the keyboard to not picked a number

                    player_word += chr(event.key).lower()

    window.blit(background_image, (0, 0))

    draw_text("Player 2, guess the word!", font, WHITE, WINDOW_WIDTH // 2, 100)
    draw_text("Word: " + " ".join("_" * len(player_word)), font, WHITE, WINDOW_WIDTH // 2, 200)

    pygame.display.update()
    
    guessed_letters = set()
    word_to_guess = player_word
    guessed_word = ["_"] * len(word_to_guess)
    remaining_attempts = 6
    # features to guess the player word
    
    while remaining_attempts > 0 and "_" in guessed_word:

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
                if event.type == pygame.KEYDOWN:
                    letter = pygame.key.name(event.key).lower()
                    if len(letter) != 1 and not letter.isalpha():
                        # verified if character string is an alphabet letter
                        draw_text("Invalid input! Please enter a single letter.", font, RED, WINDOW_WIDTH // 2, 250)
                    elif letter in guessed_letters:
                        draw_text(f"You already guessed {letter} !", font, RED, WINDOW_WIDTH // 3, 250)
                    else:
                        guessed_letters.add(letter)

                        if letter in word_to_guess:
                            for i in range(len(word_to_guess)):
                                if word_to_guess[i] == letter:
                                    guessed_word[i] = letter
                                    # defined the position of letter who were find
                        else:
                            remaining_attempts -= 1
                            # if ther is a mistake you've lost one attempt

                        waiting_for_input = False

    window.blit(background_image, (0, 0))
    
    if "_" not in guessed_word:
        pygame.mixer.music.stop()
        victory_sound.play()
        draw_text(f"Congratulations Player 2 ! The word was: {word_to_guess}", font, GREEN, WINDOW_WIDTH // 2, 100)
        scores["Player 2"] += 1
        # player 2 wins update display scores
    else:
        pygame.mixer.music.stop()
        losing_sound.play()
        draw_text(f"Sorry Player 2, you lost ! The word was: {word_to_guess}", font, RED, WINDOW_WIDTH // 2, 100)
        scores["Player 1"] += 1
        # word not find player 1 wins update display scores
        lose()
    
    draw_text("Press ENTER to return to the menu", font, WHITE, WINDOW_WIDTH // 2, 200)
    draw_text("Press SPACE to see score", font, WHITE, WINDOW_WIDTH // 2, 250) 
    draw_text("Press ECHAP to quit the game", font, WHITE, WINDOW_WIDTH // 2, 300)

    pygame.display.update()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_SPACE:
                    display_scores()
                    #input to switch between different menu

def guess_word():
    # function to play against computer
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
                if event.type == pygame.KEYDOWN:
                    letter = pygame.key.name(event.key).lower()
                    if not letter.isalpha() and len(letter) != 1:
                        draw_text("Invalid input! Please enter a single letter.", font, RED, WINDOW_WIDTH // 2, 250)
                    elif letter in use_letter:
                        draw_text("You already guessed: {letter}!", font, RED, WINDOW_WIDTH // 3, 250)
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
        pygame.mixer.music.stop()
        victory_sound.play()
        draw_text(f"Congratulations ! The word was: {guess_the_word}", font, GREEN, WINDOW_WIDTH // 2, 100)
    else:
        pygame.mixer.music.stop()
        losing_sound.play()
        draw_text(f"You lost ! The word was: {guess_the_word}", font, RED, WINDOW_WIDTH // 2, 100)
    draw_text("Press ENTER to return to the menu or ECHAP to quit", font, WHITE, WINDOW_WIDTH // 2, 200)
    lose()

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
    play_menu_music() 
    window.blit(background_image, (0, 0))

    draw_text("Welcome to Hangman!", title_font, WHITE, WINDOW_WIDTH // 2, 50)
    draw_text("This is the rules of hangman :", text_font, WHITE, WINDOW_WIDTH // 2, 125)
    draw_text("You have to find the hiding word, for that you have to give letter .", text_font, WHITE, WINDOW_WIDTH // 2, 170)
    draw_text("If you didn't find the word before all your lives gone,", text_font, WHITE, WINDOW_WIDTH // 2, 195)
    draw_text("this is the end for you .", text_font, WHITE, WINDOW_WIDTH // 2, 220)
    draw_text("So ready to play ?", text_font, WHITE, WINDOW_WIDTH // 2, 245)
    draw_text("Play Game", font, WHITE, WINDOW_WIDTH // 2, 315)
    draw_text("Player vs Player", font, WHITE, WINDOW_WIDTH // 2, 365)
    draw_text("Show Scores", font, WHITE, WINDOW_WIDTH // 2, 415)
    draw_text("Exit", font, WHITE, WINDOW_WIDTH // 2, 465)
    draw_text("Game developers : Yoel, Manuel and Jerome .", text_font, WHITE, WINDOW_WIDTH// 4, 535) 

    pygame.display.update()

    waiting_for_input = True

    while waiting_for_input:
        for event in pygame.event.get():
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
                    # change the mouse cursor depend on where it is on window

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 300 <= mouse_x <= 500:
                    if 300 <= mouse_y <= 340:
                        play_game_music()
                        guess_word()
                    elif 350 <= mouse_y <= 390:
                        play_game_music()
                        player_vs_player()
                    elif 400 <= mouse_y <= 440:
                        display_scores()
                    elif 450 <= mouse_y <= 490:
                        exit()
                        # choose what you want to do in main menu with mouse

main_menu()