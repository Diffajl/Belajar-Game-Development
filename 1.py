# game ini saya beri nama roroketan :v

import pygame
import random
import math

pygame.init()
pygame.display.set_caption("Gim")
screen = pygame.display.set_mode((500, 700))

font = pygame.font.Font(None, 36)

class Spaceship:
    def __init__(self):
        self.image = pygame.image.load("assets/spaceship.png")
        self.x = 250
        self.y = 600
        self.x_change = 0
        self.y_change = 0
        self.velocity = 1

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

        if self.x <= 0:
            self.x = 0
        elif self.x >= 490:
            self.x = 490

        if self.y <= 0:
            self.y = 0
        elif self.y >= 690:
            self.y = 690

class Bullet:
    def __init__(self):
        self.image = pygame.image.load("assets/bullet.png")
        self.x = None
        self.y = None
        self.active = False
        self.velocity = 1
        self.stock = 50

    def draw(self):
        if self.active:
            screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.active:
            self.y -= self.velocity
            if self.y <= 0:
                self.active = False

class Meteor:
    def __init__(self):
        self.image = pygame.image.load("assets/rocket.png")
        self.x = random.randint(1, 490)
        self.y = 2
        self.velocity = 0.5

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.velocity
        if self.y >= 700:
            self.x = random.randint(1, 490)
            self.y = 2

class Game:
    def __init__(self):
        self.running = True
        self.spaceship = Spaceship()
        self.bullet = Bullet()
        self.meteor = Meteor()
        self.score = 0
        self.level = 1

    def is_collision(self, x1, y1, x2, y2):
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance < 27

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord("w"):
                    self.spaceship.y_change = -self.spaceship.velocity
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    self.spaceship.x_change = -self.spaceship.velocity
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    self.spaceship.y_change = self.spaceship.velocity
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    self.spaceship.x_change = self.spaceship.velocity
                if event.key == ord("q") and not self.bullet.active and self.bullet.stock > 0:
                    self.bullet.x = self.spaceship.x
                    self.bullet.y = self.spaceship.y
                    self.bullet.active = True
                    self.bullet.stock -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == ord("w"):
                    self.spaceship.y_change = 0
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    self.spaceship.x_change = 0
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    self.spaceship.y_change = 0
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    self.spaceship.x_change = 0

    def update(self):
        self.spaceship.move()
        self.bullet.move()
        self.meteor.move()

        if self.bullet.active and self.is_collision(self.bullet.x, self.bullet.y, self.meteor.x, self.meteor.y):
            self.meteor = Meteor()
            self.score += 1
            self.bullet.active = False

        if self.score > 5:
            self.meteor.velocity = 1
            self.bullet.velocity = 1.5
            self.level = 2

        if self.score > 10:
            self.meteor.velocity = 2
            self.bullet.velocity = 2
            self.level = 3

    def draw(self):
        screen.fill((0, 0, 0))
        self.spaceship.draw()
        self.bullet.draw()
        self.meteor.draw()

        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        stock_text = font.render(f"Stok Peluru: {self.bullet.stock}", True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        screen.blit(stock_text, (10, 670))

        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            if self.bullet.stock == 0:
                self.running = False
        print(f"Game Over! Score: {self.score}")
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
