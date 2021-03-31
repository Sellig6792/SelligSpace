# from monster import Monster

import player
import pygame

class Game:

    def __init__(self):
        # Define game status
        self.is_playing = False
        # Init group for player only
        self.all_players = pygame.sprite.Group()
        # Init sprite player for game
        self.player = player.Player(self)
        # Add player in payer group
        self.all_players.add(self.player)
        # Stock last key activated
        self.pressed = {}
        # Definition new group of monsters
        self.all_mummy = pygame.sprite.Group()
        # Variable fot last spawn
        self.last_spawn = 0
        # score
        self.score = 0
        # font
        self.font = pygame.font.Font('assets/HachiMaruPop-Regular.ttf', 16)
        # pause
        self.pause = False
        self.in_menu = True

    def pauseF(self):
        self.pause = True

    def unpause(self):
        self.pause = False

    def start_game(self):
        # Start game
        self.is_playing = True
        # Spawn monster
        # self.spawn_monster()

    def game_over(self, screen):
        self.is_playing = False
        self.unpause()
        self.all_mummy = pygame.sprite.Group()
        self.player.all_bullet = pygame.sprite.Group()
        self.player.all_vie = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.bar_color = self.player.default_bar_color
        self.player.rect = self.player.default_rect
        self.pressed = {}

        self.update(screen)
        # os.system("pause")
        # self.score =

    def del_score(self):
        self.score = 0

    def update(self, screen):

        # afficher le score

        scoretext = self.font.render(f"Score {self.score}", 1, (255, 255, 255))
        screen.blit(scoretext, (20, 20))
        # Apply player sprite in game
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen, self.player.health)

        # Apply monsters sprite in game
        self.all_mummy.draw(screen)

        # Get all bullet and move it
        for bullets in self.player.all_bullet:
            bullets.move()

        for vie in self.player.all_vie:
            vie.move()
        # Get all monsters sprite in game
        for monster in self.all_mummy:
            monster.forward()
            monster.update_health_bar(screen)

        # Apply bullet
        self.player.all_bullet.draw(screen)
        self.player.all_vie.draw(screen)

        # Check player direction
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            self.player.nothing_move()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + (
                self.player.rect.width - 20) < screen.get_width() and not self.pause:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -20 and not self.pause:
            self.player.move_left()


    @staticmethod
    def check_collision_meteor(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    @staticmethod
    def check_collision_health(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)
