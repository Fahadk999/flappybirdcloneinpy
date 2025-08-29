import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 720

font = pygame.font.Font(None, 40) 

# screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def show_homescreen (screen):
    while True:
        screen.fill(pygame.Color("#61c4e8"))

        title = font.render("Flappy Circle", True, (0,0,0))
        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//3))
        screen.blit(title, title_rect)

        text = font.render("Press SPACE to Play", True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if events.type == pygame.KEYDOWN and events.key == pygame.K_SPACE:
                return


        pygame.display.flip()

        clock.tick(60)

def show_gameover (score, screen):
    while True:
        screen.fill(pygame.Color("#61c4e8"))

        title = font.render("Game Over!", True, (0,0,0))
        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//3))
        screen.blit(title, title_rect)

        score_text = font.render(f"Your Score: {score}", True, (0,0,0))
        score_text_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60))
        screen.blit(score_text, score_text_rect)

        text = font.render("Press SPACE to Play Again", True, (0,0,0))
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if events.type == pygame.KEYDOWN and events.key == pygame.K_SPACE:
                return


        pygame.display.flip()

        clock.tick(60)