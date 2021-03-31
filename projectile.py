import pygame
import constant
# from mainJeuAncien import game_var

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, x, y, game):
        super().__init__()
        # Add player in attribute
        self.player = player
        self.game = game
        # speed of bullet
        self.speed = 4
        # Definition default angle of image
        self.angle = 0
        # Bullet image for sprite
        self.image = constant.bullet_image_sprite
        # Get and set size of bullet
        self.rect = self.image.get_rect()
        self.width = 200
        self.height = 200
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Set bullet position
        self.rect.x = x
        self.rect.y = y

    def remove(self):
        # Remove actual select bullet
        self.player.all_bullet.remove(self)

    # def rotate(self):
    #     Rotate object function
        # self.angle = constant.rotate_image_angle_bullet
        # self.image = pygame.transform.rotate(self.origin_image, self.angle)

    def move(self):
        # Move bullet
        if not self.game.pause and self.game.is_playing:
            self.rect.y += self.speed
        # It's outside the screen destroy it
        if self.rect.x > constant.screen_width or self.rect.x < -50:
            self.remove()
        # If bullet enter in collision with monster remove self
        # for monster in self.player.game.check_collision(self, self.player.game.all_mummy):
        #     self.remove()
        #     monster.damage(self.player.attack, self.player, self.knowback)








class Coeur(pygame.sprite.Sprite):

    def __init__(self, player, x, game):
        super().__init__()
        # Add player in attribute
        self.player = player
        self.game = game
        # speed of bullet
        self.speed = 1
        # Definition default angle of image
        self.angle = 0
        # Bullet image for sprite
        self.image = constant.coeur_image_sprite
        # Get and set size of bullet
        self.rect = self.image.get_rect()
        self.width = 64
        self.height = 64
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Set bullet position
        self.rect.x = x
        self.rect.y = -180

    def remove(self):
        # Remove actual select bullet
        self.player.all_bullet.remove(self)

    # def rotate(self):
    #     Rotate object function
        # self.angle = constant.rotate_image_angle_bullet
        # self.image = pygame.transform.rotate(self.origin_image, self.angle)

    def move(self):
        # Move bullet
        if not self.game.pause and self.game.is_playing:
            self.rect.y += self.speed
        # It's outside the screen destroy it
        if self.rect.x > constant.screen_width or self.rect.x < -50:
            self.remove()
        # If bullet enter in collision with monster remove self
        # for monster in self.player.game.check_collision(self, self.player.game.all_mummy):
        #     self.remove()
        #     monster.damage(self.player.attack, self.player, self.knowback)