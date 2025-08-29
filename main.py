import pygame
import gameclass as gc
import random
from pygame.locals import*
import homescreen

pygame.init()

WIDTH, HEIGHT = 1200, 720

font = pygame.font.Font(None, 40) 


screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def run_game ():

    GRAVITY = 0.5
    JUMP_FORCE = -8

    all_sprites = pygame.sprite.Group()
    player = gc.Player(200, 100, GRAVITY, JUMP_FORCE)
    all_sprites.add(player)
    pipes = pygame.sprite.Group()

    def spawn_pipe (x):
        gap = 360
        pipe_variation = random.randint(180, 580)
        top_pipe = gc.Pipe(x,  pipe_variation - gap, "top")
        bot_pipe = gc.Pipe(x,  pipe_variation + gap, "bottom")

        all_sprites.add(top_pipe, bot_pipe)
        pipes.add(top_pipe, bot_pipe)

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 1200)

    global score
    score = 0

    running = True

    while running:
        
        screen.fill(pygame.Color("#61c4e8"))

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False 
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    player.jump()
            if events.type == SPAWN_EVENT:
                spawn_pipe(WIDTH + 50)
            if player.rect.top < -50 or player.rect.bottom > HEIGHT + 50:
                homescreen.show_gameover(score, screen)
                running = False

        
        all_sprites.update()
        all_sprites.draw(screen)

        if pygame.sprite.spritecollide(player, pipes, False, pygame.sprite.collide_mask):
            homescreen.show_gameover(score, screen)
            running = False

        for pipe in pipes:
            if pipe.rect.right < player.rect.left and not hasattr(pipe, "scored"):
                score += 0.5
                pipe.scored = True

        score_text = font.render(f"Score: {str(int(score))}", True, (0,0,0))
        screen.blit(score_text, (25, 7))

        
        pygame.display.update()

        clock.tick(60)


homescreen.show_homescreen(screen)

while True:
    run_game()