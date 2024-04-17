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

# Main welcome page loop
def welcome_page():
    running = True

    while running:
        screen.fill(WHITE)

        # Draw title
        draw_text("CyberSafe Seniors", FONT, BLACK, WIDTH // 2, HEIGHT // 3)

        # Draw instruction
        draw_text("Click below to start the game.", FONT, BLACK, WIDTH // 2, HEIGHT // 2)

        # Draw button
        button_rect = pygame.Rect(WIDTH // 3, HEIGHT * 2 // 3, WIDTH // 3, HEIGHT // 6)
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
def game_page():
    running = True

    while running:
        screen.fill(WHITE)

        # Draw text on the blank game page
        # draw_text("This is the game page!", FONT, BLACK, WIDTH // 2, HEIGHT // 2)

        # display images
        image = pygame.transform.scale(pygame.image.load("mountain.jpeg"), ((WIDTH//2) - WIDTH//16, HEIGHT//2 - WIDTH//16))
        
        draw_text("Option 1", FONT, BLACK, (WIDTH// 4), (HEIGHT//4) - 40)
        screen.blit(image, ((WIDTH// 32), HEIGHT//4))

        draw_text("Option 2", FONT, BLACK, (WIDTH// 2 + WIDTH//4), (HEIGHT//4) - 40)
        screen.blit(image, (WIDTH//2 + WIDTH//32, HEIGHT//4))
        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# Main function to control the flow of the program
def main():
    next_page = welcome_page()

    if next_page == "Game":
        game_page()

    pygame.quit()

if __name__ == "__main__":
    main()
