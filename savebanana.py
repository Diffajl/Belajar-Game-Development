
import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Save The Banana")

def display_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def banana(x, y):
    img = pygame.image.load("assets/banana.png")
    screen.blit(img, (x, y))

def peluru(x, y):
    img = pygame.image.load("assets/meteor.png")
    screen.blit(img, (x, y))

def collition(x1, x2, y1, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if distance < 25:
        return True
    return False

# State
START, PLAYING, GAME_OVER = 0, 1, 2
state = START

# banana
x_banana = 550
y_banana = 350
x_point_banana = 0
y_point_banana = 0
vel_banana = 5

# peluru
x_meteor = 1095
y_meteor = random.randint(1, 700)
x_point_meteor = 0
y_point_meteor = 0
vel_meteor = 5

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == START:
            if event.type == pygame.KEYDOWN:
                state = PLAYING

        if state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord("w"):
                    y_point_banana -= vel_banana
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    x_point_banana -= vel_banana
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    y_point_banana += vel_banana
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    x_point_banana += vel_banana

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == ord("w"):
                    y_point_banana = 0
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    x_point_banana = 0
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    y_point_banana = 0
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    x_point_banana = 0

        if state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == ord("q"):
                    running = False
                else:
                    x_banana = 550
                    y_banana = 350
                    x_point_banana = 0
                    y_point_banana = 0
                    x_meteor = 1095
                    y_meteor = random.randint(1, 700)
                    state = START

    if state == PLAYING:
        x_banana += x_point_banana
        y_banana += y_point_banana
        x_meteor -= vel_meteor

        if x_banana <= 0:
            x_banana = 0
        elif x_banana >= 1090:
            x_banana = 1090

        if y_banana <= 0:
            y_banana = 0
        elif y_banana >= 690:
            y_banana = 690

        if x_meteor <= 0:
            x_meteor = 1095
            y_meteor = random.randint(1, 700)

        if collition(x_banana, x_meteor, y_banana, y_meteor):
            state = GAME_OVER

        banana(x_banana, y_banana)
        peluru(x_meteor, y_meteor)

    elif state == START:
        display_text("Press any key to start", 60, (255, 255, 255), 300, 300)

    elif state == GAME_OVER:
        display_text("Anda kalah!", 60, (255, 255, 255), 400, 300)
        display_text("Press 'Q' to quit or any key to play again", 60, (255, 255, 255), 100, 400)

    pygame.display.update()

pygame.quit()
