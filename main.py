import enum
import struct
import random

import pygame
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 1200
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 40)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CyberSafe Seniors")

# Function to display text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to create a button
def draw_button(text, font, color, rect):
    pygame.draw.rect(screen, BLACK, rect, 2)
    draw_text(text, font, color, rect.centerx, rect.centery)

class QuestionTypes(enum.Enum):
    PHISH = 1
    NOT_A_PHISH = 2

# Main welcome page loop
def welcome_page(highscore):
    running = True

    while running:
        screen.fill(WHITE)

        # Draw title
        draw_text("CyberSafe Seniors", FONT, BLACK, WIDTH / 2, HEIGHT / 3)

        # Draw instruction
        draw_text("Click below to start the game.", FONT, BLACK, WIDTH / 2, HEIGHT / 2)

        draw_text(f"Previous Highscore: {highscore}", FONT, BLACK, WIDTH / 2, HEIGHT - 15)

        # Draw button
        button_rect = pygame.Rect(WIDTH / 3, HEIGHT * 2 / 3, WIDTH / 3, HEIGHT / 6)
        draw_button("Game", FONT, BLACK, button_rect)

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if button_rect.collidepoint(x, y):
                    return "Game"

# Blank game page loop
def game_page(highscore):
    running = True
    score = 0

    # Load initial image
    true_answer = random.choice(list(QuestionTypes))
    image_filename = ""
    if true_answer == QuestionTypes.PHISH:
        image_filename = random.choice(["1-PHISH.png", "2-PHISH.png"])
    else:
        image_filename = random.choice(["1-NOT_PHISH.png", "2-NOT_PHISH.png"])
    image = pygame.transform.scale(pygame.image.load(f"resources/{image_filename}"), ((WIDTH / 2) - WIDTH / 16, HEIGHT / 2))

    while running:
        screen.fill(WHITE)

        # Display the question text, image, and current score
        draw_text("Is this a phishing attempt?", FONT, BLACK, (WIDTH / 2), (HEIGHT/4) - 40)
        screen.blit(image, ((WIDTH / 2) - (image.get_width() / 2), HEIGHT/4))
        draw_text(f"Score: {score}", FONT, BLACK, (WIDTH - 100), 20)

        # Draw buttons
        button_yes = pygame.Rect(WIDTH / 5 - (WIDTH / 3)/2, HEIGHT * 5 / 6, WIDTH / 3, HEIGHT / 7)
        draw_button("Yes", FONT, BLACK, button_yes)

        button_no = pygame.Rect(WIDTH - (WIDTH / 5) - (WIDTH / 3)/2, HEIGHT * 5 / 6, WIDTH / 3, HEIGHT / 7)
        draw_button("No", FONT, BLACK, button_no)

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return score if score > highscore else highscore
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if button_yes.collidepoint(x, y) or button_no.collidepoint(x, y):
                    # Choose a random image file based on the true answer
                    if true_answer == QuestionTypes.PHISH:
                        image_filename = random.choice(["1-PHISH.png", "2-PHISH.png", "3-PHISH.png", "4-PHISH.png", "5-PHISH.png"])
                    else:
                        image_filename = random.choice(["1-NOT_PHISH.png", "2-NOT_PHISH.png", "3-NOT_PHISH.png", "4-NOT_PHISH.png", "5-NOT_PHISH.png",])

                    # Display the selected image
                    image = pygame.transform.scale(pygame.image.load(f"resources/{image_filename}"), ((WIDTH / 2) - WIDTH / 16, HEIGHT / 2))

                    # Check the answer and update the score
                    if (button_yes.collidepoint(x, y) and true_answer == QuestionTypes.PHISH) or \
                       (button_no.collidepoint(x, y) and true_answer == QuestionTypes.NOT_A_PHISH):
                        score += 1
                    else:
                        print("loss")

    return score if score > highscore else highscore

    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        true_answer = random.choice(list(QuestionTypes))

        # Display the question text and current score
        draw_text("Is this a phishing attempt?", FONT, BLACK, (WIDTH / 2), (HEIGHT/4) - 40)
        draw_text(f"Score: {score}", FONT, BLACK, (WIDTH - 100), 20)

        # Draw buttons
        button_yes = pygame.Rect(WIDTH / 5 - (WIDTH / 3)/2, HEIGHT * 5 / 6, WIDTH / 3, HEIGHT / 7)
        draw_button("Yes", FONT, BLACK, button_yes)

        button_no = pygame.Rect(WIDTH - (WIDTH / 5) - (WIDTH / 3)/2, HEIGHT * 5 / 6, WIDTH / 3, HEIGHT / 7)
        draw_button("No", FONT, BLACK, button_no)

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return score if score > highscore else highscore
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if button_yes.collidepoint(x, y) or button_no.collidepoint(x, y):
                    # Choose a random image file based on the true answer
                    image_filename = ""
                    if true_answer == QuestionTypes.PHISH:
                        image_filename = random.choice(["1-PHISH.png", "2-PHISH.png"])
                    else:
                        image_filename = random.choice(["1-NOT_PHISH.png", "2-NOT_PHISH.png"])

                    # Display the selected image
                    image = pygame.transform.scale(pygame.image.load(f"resources/{image_filename}"), ((WIDTH / 2) - WIDTH / 16, HEIGHT / 2 - WIDTH / 16))
                    screen.blit(image, ((WIDTH / 2) - (image.get_width() / 2), HEIGHT/4))

                    # Check the answer and update the score
                    if (button_yes.collidepoint(x, y) and true_answer == QuestionTypes.PHISH) or \
                       (button_no.collidepoint(x, y) and true_answer == QuestionTypes.NOT_A_PHISH):
                        score += 1
                    else:
                        print("loss")

    return score if score > highscore else highscore

    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        true_answer = random.choice(list(QuestionTypes))

        # Choose a random image file based on the true answer
        image_filename = ""
        if true_answer == QuestionTypes.PHISH:
            image_filename = random.choice(["1-PHISH.png", "2-PHISH.png"])
        else:
            image_filename = random.choice(["1-NOT_PHISH.png", "2-NOT_PHISH.png"])

        # Display the selected image
        image = pygame.transform.scale(pygame.image.load(f"resources/{image_filename}"), ((WIDTH / 2) - WIDTH / 16, HEIGHT / 2 - WIDTH / 16))
        draw_text("Is this a phishing attempt?", FONT, BLACK, (WIDTH / 2), (HEIGHT/4) - 40)
        screen.blit(image, ((WIDTH / 2) - (image.get_width() / 2), HEIGHT/4))
        draw_text(f"Score: {score}", FONT, BLACK, (WIDTH - 100), 20)

        # Draw buttons
        button_yes = pygame.Rect(WIDTH / 5 - (WIDTH / 3)/2, HEIGHT * 5 / 6, WIDTH / 3, HEIGHT / 7)
        draw_button("Yes", FONT, BLACK, button_yes)

        button_no = pygame.Rect(WIDTH - (WIDTH / 5) - (WIDTH / 3)/2, HEIGHT * 5 / 6, WIDTH / 3, HEIGHT / 7)
        draw_button("No", FONT, BLACK, button_no)

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return score if score > highscore else highscore
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if button_yes.collidepoint(x, y):
                    if true_answer == QuestionTypes.PHISH:
                        score += 1
                    else:
                        print("loss")
                elif button_no.collidepoint(x, y):
                    if true_answer == QuestionTypes.NOT_A_PHISH:
                        score += 1
                    else:
                        print("loss")

    return score if score > highscore else highscore

# Main function to control the flow of the program
def main():
    # setup
    highscore = 0
    if(os.path.exists("playerdata/playerdata.dat")):
        with open("playerdata/playerdata.dat", 'r') as file:
            lines = file.readlines()
            if len(lines) != 0:
                highscore = int(lines[0])

    next_page = welcome_page(highscore)

    if next_page == "Game":
        with open("playerdata/playerdata.dat", 'w') as file:
            file.write(str(game_page(highscore)))

    pygame.quit()

if __name__ == "__main__":
    main()