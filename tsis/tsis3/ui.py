import pygame
from persistence import load_leaderboard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def get_font():

    return pygame.font.SysFont(
        "Verdana",
        18
    )


def draw_text(screen, text, x, y):

    font = get_font()

    screen.blit(
        font.render(
            text,
            True,
            BLACK
        ),
        (x, y)
    )


def draw_menu(screen):

    screen.fill(WHITE)

    draw_text(
        screen,
        "TSIS 3 RACER",
        130,
        150
    )

    draw_text(
        screen,
        "1 - Play",
        150,
        250
    )

    draw_text(
        screen,
        "2 - Leaderboard",
        150,
        300
    )

    draw_text(
        screen,
        "3 - Settings",
        150,
        350
    )

    

def draw_settings(screen, settings):

    screen.fill(WHITE)

    draw_text(
        screen,
        "SETTINGS",
        150,
        150
    )

    draw_text(
        screen,
        f"Sound: {settings['sound']}",
        120,
        250
    )

    draw_text(
        screen,
        "S - Toggle sound",
        100,
        400
    )

    draw_text(
        screen,
        "ESC - Back",
        100,
        500
    )


def draw_leaderboard(screen):

    screen.fill(WHITE)

    data = load_leaderboard()

    draw_text(
        screen,
        "LEADERBOARD",
        130,
        80
    )

    y = 150

    for i, row in enumerate(data):

        text = (
            f"{i+1}. "
            f"{row['name']}  "
            f"Score:{row['score']}  "
            f"Dist:{row['distance']}"
        )

        draw_text(
            screen,
            text,
            40,
            y
        )

        y += 30

    draw_text(
        screen,
        "ESC - Back",
        140,
        520
    )


def draw_game_over(screen, score, distance):

    screen.fill(WHITE)

    draw_text(
        screen,
        "GAME OVER",
        140,
        200
    )

    draw_text(
        screen,
        f"Score: {score}",
        140,
        260
    )

    draw_text(
        screen,
        f"Distance: {distance}",
        120,
        300
    )

    draw_text(
        screen,
        "R - Retry",
        150,
        380
    )

    draw_text(
        screen,
        "M - Menu",
        150,
        420
    )