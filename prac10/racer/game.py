import pygame
import sys
from pygame.locals import *
import random

pygame.init()
pygame.mixer.init()

FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 5
SCORE = 0

# ================= ФОН =================

background = pygame.image.load("AnimatedStreet.png")
background = pygame.transform.scale(
    background,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Фон Game Over
game_over_bg = pygame.image.load("game_over_bg.png")
game_over_bg = pygame.transform.scale(
    game_over_bg,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

bg_y1 = 0
bg_y2 = -SCREEN_HEIGHT

DISPLAYSURF = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Racer Game")

# ================= ШРИФТЫ =================

font_big = pygame.font.SysFont("Verdana", 60)
font_medium = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)

# ================= PLAYER =================

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load(
            "Player.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (90, 100)
        )

        self.rect = self.image.get_rect()

        self.rect.center = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 150
        )

        self.hitbox = self.rect.inflate(-40, -20)

    def move(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:

            if self.rect.left > 0:
                self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:

            if self.rect.right < SCREEN_WIDTH:
                self.rect.move_ip(5, 0)

        self.hitbox.center = self.rect.center


# ================= ENEMY =================

class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load(
            "Enemy.png"
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (90, 100)
        )

        self.rect = self.image.get_rect()

        self.hitbox = self.rect.inflate(-40, -20)

        self.reset_position()

    def reset_position(self):

        lanes = [50, 150, 250, 350]

        self.rect.center = (
            random.choice(lanes),
            -100
        )

    def move(self):

        global SCORE

        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:

            SCORE += 1
            self.reset_position()

        self.hitbox.center = self.rect.center


# ================= ОБЪЕКТЫ =================

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# ================= GAME LOOP =================

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            sys.exit()

        if event.type == INC_SPEED:

            if SPEED < 15:
                SPEED += 0.5

    # движение фона

    bg_y1 += SPEED
    bg_y2 += SPEED

    if bg_y1 >= SCREEN_HEIGHT:
        bg_y1 = -SCREEN_HEIGHT

    if bg_y2 >= SCREEN_HEIGHT:
        bg_y2 = -SCREEN_HEIGHT

    DISPLAYSURF.blit(background, (0, bg_y1))
    DISPLAYSURF.blit(background, (0, bg_y2))

    # SCORE

    score_text = font_small.render(
        "Score: " + str(SCORE),
        True,
        BLACK
    )

    DISPLAYSURF.blit(score_text, (10, 10))

    # движение объектов

    for entity in all_sprites:

        entity.move()

        DISPLAYSURF.blit(
            entity.image,
            entity.rect
        )


    # СТОЛКНОВЕНИЕ

    for enemy in enemies:

        if P1.hitbox.colliderect(enemy.hitbox):

            pygame.mixer.Sound(
                "crash.mp3"
            ).play()

            game_over_screen = True

            while game_over_screen:

                DISPLAYSURF.blit(
                    game_over_bg,
                    (0, 0)
                )

                

                score_text = font_medium.render(
                    f"Score: {SCORE}",
                    True,
                    WHITE
                )

                DISPLAYSURF.blit(
                    score_text,
                    (165, 240)
                )

                restart_text = font_medium.render(
                    "Press R to Restart",
                    True,
                    WHITE
                )

                DISPLAYSURF.blit(
                    restart_text,
                    (109, 460)
                )

                exit_text = font_medium.render(
                    "Press ESC to Exit",
                    True,
                    WHITE
                )

                DISPLAYSURF.blit(
                    exit_text,
                    (109, 500)
                )

                pygame.display.update()

                for event in pygame.event.get():

                    if event.type == QUIT:

                        pygame.quit()
                        sys.exit()

                    if event.type == KEYDOWN:

                        if event.key == K_r:

                            SCORE = 0
                            SPEED = 5

                            P1.rect.center = (
                                SCREEN_WIDTH // 2,
                                SCREEN_HEIGHT - 150
                            )

                            for enemy in enemies:
                                enemy.reset_position()

                            game_over_screen = False

                        if event.key == K_ESCAPE:

                            pygame.quit()
                            sys.exit()

    pygame.display.update()

    FramePerSec.tick(FPS)