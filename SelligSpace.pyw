import pygame
import math
import constant
import game
from tkinter import *

screen_width = constant.screen_width
screen_height = constant.screen_height
background = constant.background_default

banner = constant.banner_default

banner_rect = banner.get_rect()

# 455 / 133
running = True

pygame.init()

# Generate screen of game

pygame.display.set_caption(constant.game_name)
screen = pygame.display.set_mode((screen_width, screen_height))

banner_rect.x = math.ceil(screen.get_width() / 2) - 227
banner_rect.y = math.ceil(screen.get_height()) - 133

# Generate button
# play_button = pygame.image.load('assets/banner.png')
# play_button = pygame.transform.scale(play_button, (400, 150))
# play_button_rect = play_button.get_rect()
# play_button_rect.x = math.ceil(screen.get_width() / 3.33)
# play_button_rect.y = math.ceil(screen.get_height() / 1.6)

game_var = game.Game()

i2 = 0
coorx = [0]
coory = [0]
# i = 0
# while i <= 1060:
#     try:
#         if i % 20 == 0:
#             coorx.append(i)
#     except ZeroDivisionError:
#         coorx.append(i)

i = -200
while i < 0:
    coory.append(i)
    i += 1
i = 0
sc = 0
while running:
    for event in pygame.event.get():
        # Exit event
        if event.type == pygame.QUIT:
            # Exit game
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_var.pauseF()
                break
            if event.key == pygame.K_SPACE and game_var.is_playing:
                game_var.pause = False
                game_var.start_game()
                game_var.is_playing = True

    # print(game_var.is_playing, "-----", game_var.pause)

    # if game_var.in_menu and game_var.is_playing and game_var.pause:
    # game_var.unpause()
    # time.sleep(5)
    # print("az")
    # screen.blit(banner, banner_rect)
    # os.system("pause")

    if not game_var.pause:
        p = 0
        sc += 0.5
        if sc / 2 == 1:
            if game_var.is_playing and not game_var.pause:
                game_var.score += int(str(sc).split(".")[0])
                # print("-->", sc, "-->", game_var.score)
                sc = 0
            elif not game_var.is_playing and not game_var.pause:
                sc = 0
        for meteor in game_var.player.all_bullet:
            if meteor.rect.y > 780 and game_var.is_playing and not game_var.pause:
                meteor.remove()
                # print("remove")
                # print(game_var.player.all_bullet)
        for vie in game_var.player.all_vie:
            if vie.rect.y > 780 and game_var.is_playing and not game_var.pause:
                vie.remove()

        if game_var.check_collision_meteor(game_var.player, game_var.player.all_bullet) and \
                not game_var.pause:
            game_var.player.damage(20, screen)
        if game_var.check_collision_health(game_var.player, game_var.player.all_vie) and \
                not game_var.pause:
            game_var.player.add_health(20)

        i2 += 1
        i += 1
        # print(i)
        p = game_var.score / 1000
        if p < 1:
            p = 1
        if p > 3:
            p = 3
        if i % 200 == 0 and game_var.is_playing and not game_var.pause:
            # print(p, "----------------", i, "----------------", game_var.player.score)
            game_var.player.fire(i, coory, p, game_var)

        # Apply background to game
        try:
            screen.blit(background, (0, 0))
        except:
            break

        # Start game if is_playing is true
        if game_var.is_playing and not game_var.pause:
            game_var.update(screen)

        elif game_var.pause:
            screen.blit(banner, banner_rect)
            game_var.update(screen)


        else:
            # screen.blit(play_button, play_button_rect)
            # print(type(screen.get_rect()))

            screen.blit(banner, banner_rect)
            oscore = str(game_var.score).split(".")
            score = int(oscore[0])
            # game_var.pause = True
            # print(oscore[0], "--", score, "--", type(oscore[0]), type(score))
            overscore = pygame.font.SysFont('lato', 60, True).render(f"Score Final: {oscore[0]}", 50, (255, 255, 255))
            i = 0
            if score != 0:
                # print(overscore.get_rect())

                screen.blit(overscore, (
                    int(screen.get_width() / 2) - int(overscore.get_width() / 2), int(screen.get_height() / 2)))
                # game_var.score = 0

                # ------------------------------------------------------------------------------------
                while True:

                    if game_var.pause:
                        game_var.pauseF()
                        highscores = Tk()
                        highscores.title("CUOUC")
                        game_var.unpause()
                        highscores.mainloop()

                    for event in pygame.event.get():
                        # Exit event
                        if event.type == pygame.QUIT:
                            # Exit game
                            running = False
                            pygame.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                game_var.pauseF()

                                break
                            if event.key == pygame.K_SPACE:
                                game_var.pause = False
                                game_var.del_score()
                                game_var.start_game()
                                game_var.is_playing = True
                            else:
                                continue
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            # print(pygame.mouse.get_pos())
                            if banner_rect.collidepoint(event.pos):
                                game_var.del_score()
                                game_var.unpause()
                                game_var.start_game()

                                continue
                            else:
                                continue
                        else:
                            continue
                    break
                    # if game_var.pause:
                    #     highscores = Tk()
                    #     highscores.title("High Scores")
                    #     scoreslabel = Label(text="", font=("Lato", 20))
                    #     with open('scores.txt', 'r+') as f:
                    #         scoresr = f.readlines()
                    #     scores = []
                    #     for score in scoresr:
                    #
                    #         scores.append(int(score.rstrip()))
                    #
                    #     ls = []
                    #
                    #     for count, char in enumerate(scores):
                    #         maxs = max(scores)
                    #
                    #         print(count, char)
                    #         a = scoreslabel.cget('text')
                    #         try:
                    #             print(ls[9])
                    #         except:
                    #
                    #
                    #             scoreslabel.configure(text=a + "\n" + str(maxs))
                    #             ls.append(maxs)
                    #             del scores[count]

                    for score in scores:
                        # print(score.rstrip())

                        scoreslabel.pack()
                    game_var.pauseF()

                    game_var.unpause()
                    while True:
                        try:
                            highscores.update()
                        except TclError:
                            pass

                    highscores.mainloop()
            # overscore = game_var.font.render(f"Score Final : {game_var.score}", 1, (255, 255, 255))
            # screen.blit(overscore, (540, 360))
            # game_var.scoreAppli(screen)

        # Update screen of game
        try:
            pygame.display.flip()
        except pygame.error:
            pass

        # if not game_var.is_playing:
        #     game_var.score = 0

        # Get all event

        # Exit event
        if event.type == pygame.QUIT:
            # Exit game
            # game_var.game_over()
            running = False
            pygame.quit()
        # Check press key of keyboard
        elif event.type == pygame.KEYDOWN:
            # Save actual press key
            game_var.pressed[event.key] = True
            # Fire ball in press space
            if event.key == pygame.K_SPACE and not game_var.is_playing:
                game_var.score = 0
                game_var.start_game()
                game_var.is_playing = True
                game_var.pause = False

            if event.key == pygame.K_SPACE and game_var.pause:
                game_var.pause = False
                game_var.is_playing = True
            if event.key == pygame.K_ESCAPE and game_var.is_playing is True:
                print("ok+")
                game_var.pauseF()
            # Disable press key
        elif event.type == pygame.KEYUP:
            game_var.pressed[event.key] = False
            # Detection event mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            if banner_rect.collidepoint(event.pos):
                game_var.del_score()
                game_var.start_game()
                game_var.is_playing = True
                game_var.score = 0
                game_var.pause = False
