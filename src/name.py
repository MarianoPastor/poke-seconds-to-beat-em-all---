import pygame
import sys
from constants import *

class Name:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.text_input = ""

    def name_input(self):
        while True:
            self.screen.fill(YELLOW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return self.text_input
                    elif event.key == pygame.K_BACKSPACE:
                        self.text_input = self.text_input[:-1]
                    else:
                        self.text_input += event.unicode

            text_surface = self.font.render(f"What's your name?: {self.text_input}", True, BLACK)
            rect = text_surface.get_rect()
            rect.center = (WIDTH // 2, HEIGHT // 2)
            self.screen.blit(text_surface, rect)

            pygame.display.flip()