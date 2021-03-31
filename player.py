import pygame
import constant
from projectile import Projectile, Coeur
import random


# Player class (all function for all player)

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        # Basic and max health point
        self.health = 100
        self.max_health = 100
        # Basic attack point
        self.attack = 10
        # Basic player speed
        self.speed = 3
        # Default player score
        self.score = 0
        # Bullet def
        self.all_players = pygame.sprite.Group()

        self.all_bullet = pygame.sprite.Group()
        self.all_vie = pygame.sprite.Group()
        # Image for player sprite
        self.image = pygame.transform.scale(pygame.image.load('assets/player.png'), (200, 200))
        # self.image = pygame.transform.scale(self.image, 50, 50)
        self.rect = self.image.get_rect()
        # Set default position on screen
        self.rect.x = (constant.screen_width / 2) - self.rect.width / 2
        self.rect.y = constant.screen_height - 215
        self.default_rect = self.rect
        # Definition of life bar color (rgb)
        self.bar_color = (111, 210, 46)
        self.default_bar_color = (111, 210, 46)
        self.background_bar_color = (0, 0, 0)

        # count
        self.count = 0
        # bar pos


    def update_health_bar(self, surface, health):
        # check health
        pos = self.image.get_width() / 2 - 50
        if health > self.max_health:
            pos = self.image.get_width() / 2 - health / 2
        if self.health <= 20:
            self.bar_color = (255, 0, 0)
        elif self.health <= 40:
            self.bar_color = (255, 102, 0)
        elif self.health <= 60:
            self.bar_color = (239, 207, 16)
        elif self.health <= 80:
            self.bar_color = (179, 238, 9)
        elif self.health <= 100:
            self.bar_color = self.default_bar_color
        elif self.health > 100:
            self.bar_color =(9, 58, 238)
        # Definition of life bar position
        bar_position = [self.rect.x + pos, self.rect.y + 200, self.health, 5]
        background_bar_position = [self.rect.x + pos, self.rect.y + 200, self.max_health, 5]

        # Draw life bar
        pygame.draw.rect(surface, self.background_bar_color, background_bar_position)
        pygame.draw.rect(surface, self.bar_color, bar_position)

    def damage(self, amount, screen):
        if self.health > 0:
            self.health -= amount
        else:
            self.bar_color = (0, 0, 0)

        if self.health < 1:
            # self.game.all_players.remove(self)
            # game_var.score = 0
            self.game.game_over(screen)
            # game_var.score = 0

    def add_health(self, amount):
        if self.health < 120:
            self.health += amount


    def fire(self, i, coory, number, game):
        # Create new bullet in the game
        coorx = []
        addx = self.rect.x - 250
        while addx < self.rect.x + 251:
            if addx % 30 == 0:
                coorx.append(addx)
            # print(coorx)
            # print(self.rect.x)
            addx += 1
            # print(self.rect.x)
            # print(coorx)
        # os.system("pause")
        i2 = 0
        i3 = 5000
        p = number - random.randrange(0, 2)
        if p == 0:
            p = 1
        while i > i3:
            p += 1
            i3 += 5000

        # print(p)
        while i2 < p:
            coor = random.choice(coorx)
            bullet = Projectile(self, int(coor), random.choice(coory), game)
            # print(coor, "-", self.rect.x)
            self.all_bullet.add(bullet)
            i2 += 1

        if i % 5000 == 0:
            vie = Coeur(self, random.randrange(-100, 1016), game)
            self.all_vie.add(vie)
        del coorx

    def nothing_move(self):
        # Don't move player
        self.rect.x = self.rect.x

    def move_right(self):
        # Check mummy collision
        # Move player in right
        self.rect.x += self.speed

    def move_left(self):
        # Move player in left
        self.rect.x -= self.speed