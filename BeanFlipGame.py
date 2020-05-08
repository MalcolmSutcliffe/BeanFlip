import Game
import pygame
import sys
import PlayerRandom
import PlayerHighScore
import PlayerMostSwaps
import PlayerLargestLead
import time

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
dark_grey = (64, 64, 64)
light_grey = (196, 196, 196)

pygame.init()
pygame.display.set_caption("BeanFlip")
screen = pygame.display.set_mode((1000, 1000))
sans = pygame.font.Font('freesansbold.ttf', 20)
title = pygame.font.Font('freesansbold.ttf', 60)


def main_menu():

    button_game_pvp = (300, 300, 400, 100)
    button_game_ai = (300, 450, 400, 100)
    button_settings = (300, 600, 400, 100)
    button_quit_game = (300, 750, 400, 100)

    run_menu = True

    while run_menu:

        screen.fill(light_grey)
        draw_text("Bean Flip", title, black, screen, 500, 200)
        draw_button("Player vs. Player", sans, black, grey, screen, button_game_pvp,
                    check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_game_pvp))
        draw_button("Player vs. Computer", sans, black, grey, screen, button_game_ai,
                    check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_game_ai))
        draw_button("Settings", sans, black, grey, screen, button_settings,
                    check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_settings))
        draw_button("Quit Game", sans, black, grey, screen, button_quit_game,
                    check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_quit_game))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_game_pvp):
                    game_pvp()
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_game_ai):
                    ai_menu()
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_settings):
                    pass
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_quit_game):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def ai_menu():

    run_ai_menu = True

    button_ai_colour_white = (398, 296, 100, 100)
    button_ai_colour_white_outline = (394, 292, 108, 108)
    button_ai_colour_black = (502, 296, 100, 100)
    button_ai_colour_black_outline = (498, 292, 108, 108)

    button_ai_difficulty_1 = (371, 600, 48, 48)
    button_ai_difficulty_2 = (423, 600, 48, 48)
    button_ai_difficulty_3 = (475, 600, 48, 48)
    button_ai_difficulty_4 = (527, 600, 48, 48)
    button_ai_difficulty_5 = (579, 600, 48, 48)

    button_start_game = (300, 800, 400, 100)

    ai_colour = 1
    ai_difficulty = 1

    while run_ai_menu:

        screen.fill(light_grey)

        if ai_colour == 0:
            pygame.draw.rect(screen, dark_grey, button_ai_colour_white_outline)
        elif ai_colour == 1:
            pygame.draw.rect(screen, dark_grey, button_ai_colour_black_outline)
        pygame.draw.rect(screen, white, button_ai_colour_white)
        pygame.draw.rect(screen, black, button_ai_colour_black)

        draw_text("Computer Colour:", sans, black, screen, 500, 250)

        draw_text("Difficulty:", sans, black, screen, 500, 550)

        draw_button("1", sans, black, grey, screen, button_ai_difficulty_1, ai_difficulty == 1)
        draw_button("2", sans, black, grey, screen, button_ai_difficulty_2, ai_difficulty == 2)
        draw_button("3", sans, black, grey, screen, button_ai_difficulty_3, ai_difficulty == 3)
        draw_button("4", sans, black, grey, screen, button_ai_difficulty_4, ai_difficulty == 4)
        draw_button("5", sans, black, dark_grey, screen, button_ai_difficulty_5, ai_difficulty == 5)

        draw_button("Go", sans, black, grey, screen, button_start_game, check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_start_game))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_ai_menu = False
            if event.type == pygame.MOUSEBUTTONUP:
                if check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_colour_white):
                    ai_colour = 0
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_colour_black):
                    ai_colour = 1
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_difficulty_1):
                    ai_difficulty = 1
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_difficulty_2):
                    ai_difficulty = 2
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_difficulty_3):
                    ai_difficulty = 3
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_difficulty_4):
                    ai_difficulty = 4
                # elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_difficulty_5):
                #     ai_difficulty = 5
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_ai_difficulty_1):
                    ai_difficulty = 1
                elif check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], button_start_game):
                    ai = None
                    if ai_difficulty == 1:
                        ai = PlayerRandom.make_player(ai_colour)
                    elif ai_difficulty == 2:
                        ai = PlayerHighScore.make_player(ai_colour)
                    elif ai_difficulty == 3:
                        ai = PlayerMostSwaps.make_player(ai_colour)
                    elif ai_difficulty == 4:
                        ai = PlayerLargestLead.make_player(ai_colour)
                    run_ai_menu = False
                    game_ai(ai_colour, ai)

        pygame.display.update()


def game_pvp():

    game = Game.make_game()

    run_game = True

    while run_game:

        for event in pygame.event.get():

            player_turn(event, game)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_game = False

        draw_game(screen, game)


def game_ai(ai_colour, ai_playstyle):

    game = Game.make_game()

    run_game = True

    draw_game(screen, game)

    while run_game:

        if game.turn == ai_colour:
            ai_playstyle.play_move(game)
            time.sleep(1)

        for event in pygame.event.get():

            player_turn(event, game)

            # check if game over

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_game = False

            draw_game(screen, game)


def player_turn(event, game):

    if event.type == pygame.MOUSEBUTTONUP:

        # check if clicked on board
        for row in game.board:
            for t in row:

                if check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], t.collision_rect):

                    # check if there was a piece selected, then play it
                    for x in game.players[game.turn].piece_set:
                        if x.is_selected:
                            game.play(t.coordinates, x.piece_type)

        # check if clicked on piece
        for x in game.players[game.turn].piece_set:
            if check_collision(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], x.collision_rect):
                # unselect all other pieces
                for y in game.players[game.turn].piece_set:
                    y.is_selected = False
                # select current piece
                x.is_selected = True
                break


def draw_button(text, font, text_colour, button_colour, surface, rect, selected):
    if selected:
        outline_rect = (rect[0]-4, rect[1]-4, rect[2]+8, rect[3]+8)
        pygame.draw.rect(surface, black, outline_rect)
    pygame.draw.rect(surface, button_colour, rect)
    draw_text(text, font, text_colour, screen, rect[0] + rect[2] // 2, rect[1] + rect[3] // 2)


def draw_text(text, font, colour, surface, x, y):
    text_obj = font.render(text, True, colour)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def draw_game(surface, game):

    game_over = True

    score = game.score()

    for row in game.board:
        for t in row:
            if t.can_play:
                game_over = False

    screen.fill(light_grey)
    game.players[0].draw_pieces(surface)
    game.players[1].draw_pieces(surface)
    game.draw_board(screen)

    # text
    draw_text(str(score[0]), sans, white, surface, 860, 500)
    draw_text(str(score[1]), sans, black, surface, 900, 500)
    draw_text("Black Pieces:", sans, black, surface, 500, 960)
    draw_text("It is:", sans, black, surface, 120, 465)
    draw_text("Turn", sans, black, surface, 120, 535)
    draw_text("Score:", sans, black, surface, 880, 465)
    draw_text("White Pieces:", sans, black, surface, 500, 40)

    if game_over:
        draw_text("Game Over!", title, black, surface, 500, 100)
        game.turn = -1

        if score[0] > score[1]:
            draw_text("White Wins!", title, black, surface, 500, 175)
        elif score[0] < score[1]:
            draw_text("Black Wins!", title, black, surface, 500, 175)
        elif score[0] == score[1]:
            draw_text("Tie!", title, black, surface, 500, 175)

    if game.turn == 0:
        draw_text("White's", sans, white, surface, 120, 500)
    else:
        draw_text("Black's", sans, black, surface, 120, 500)

    pygame.display.update()


def check_collision(x, y, rect):
    return rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]


main_menu()
