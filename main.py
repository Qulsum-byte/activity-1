import pygame
import random
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
GREEN = (0, 200, 100)
RED = (255, 50, 50)

# Font
font = pygame.font.SysFont(None, 36)


class Button:
    def __init__(self, text, x, y, w, h, color, action):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"


# Game data
choices = ["Rock", "Paper", "Scissors"]
result = "Choose Rock, Paper, or Scissors"

# Buttons
buttons = [
    Button("Rock", 80, 300, 120, 50, BLUE, "Rock"),
    Button("Paper", 240, 300, 120, 50, GREEN, "Paper"),
    Button("Scissors", 400, 300, 120, 50, RED, "Scissors"),
]

# Game loop
running = True
while running:
    screen.fill((240, 240, 240))  # background color

    # Title
    title = font.render("Rock Paper Scissors", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

    # Result text
    result_text = font.render(result, True, BLACK)
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 120))

    # Draw buttons
    for button in buttons:
        button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_clicked(pos):
                    player_choice = button.action
                    computer_choice = random.choice(choices)
                    result = f"You: {player_choice} | Computer: {computer_choice} → {get_winner(player_choice, computer_choice)}"

    pygame.display.flip()
