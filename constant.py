import pygame
import game
from player import Player
from os import getcwd
# This fil save all constants variables
directory = getcwd().replace('\\', "/") + "/"
print(directory)
# Screen variables
screen_width = 1080
screen_height = 720

# Game variables
game_name = "Sellig's Space"
background_default = pygame.image.load(f'{directory}assets/bg.jpg')
banner_default = pygame.image.load(f'{directory}assets/banner.png')
player_image_sprite = pygame.image.load(f'{directory}assets/player.png')
player_image_sprite = pygame.transform.scale(player_image_sprite, (300, 300))
bullet_image_sprite = pygame.image.load(f'{directory}assets/meteor.png')
coeur_image_sprite = pygame.image.load(f'{directory}assets/vie.png')
menu_image_sprite = pygame.image.load(f'{directory}assets/menu.png')
rotate_image_angle_bullet = 180
default_mummy_posX = 1000
default_mummy_posY = screen_height - (265 - (Player(game).rect.width/4))