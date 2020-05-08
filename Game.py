import Tile
import Player
import pygame
import random
import copy

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
dark_grey = (64, 64, 64)
darker_grey = (80, 80, 80)
light_grey = (196, 196, 196)


class Game:
    # who's turn it is (0 = white, 1 = black)
    turn = 0

    def __init__(self, player1=None, player2=None):
        # board is a 5x5 grid each cell should contain a colour
        # and whether or not that cell can be played on.
        # colors: -1 = grey, 0 = white, 1 = black
        self.board = [[Tile.make_tile(coordinates=[i, j]) for j in range(5)] for i in range(5)]
        # can't play on the middle square
        self.board[2][2].can_play = False
        # initialize 2 players
        if player1 is None:
            player1 = Player.make_player(0)
        if player2 is None:
            player2 = Player.make_player(1)

        self.players = [player1, player2]

    def play(self, coordinates, piece_type, do_print=False):

        row = coordinates[0]
        column = coordinates[1]

        play_tile = self.board[row][column]
        if not play_tile.can_play:
            if do_print:
                print("Error: Tile cannot be played on!")
            return
        if not self.players[self.turn].piece_set[piece_type - 1].playable:
            if do_print:
                print("Error: Piece " + piece_type + " has already been used!")
            return

        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.players[self.turn].piece_set[piece_type - 1].swap_grid[i + 1][j + 1]:
                    if 0 <= row + i < 5 and 0 <= column + j < 5:
                        if self.board[row + i][column + j].colour == -1:
                            self.board[row + i][column + j].colour = self.turn
                        else:
                            self.board[row + i][column + j].colour = 1 - self.board[row + i][column + j].colour

        self.players[self.turn].piece_set[piece_type - 1].playable = False

        play_tile.can_play = False

        self.turn = 1 - self.turn

    def print_board(self):
        print("y= _____ _____ _____ _____ _____")
        i = 5
        for row in self.board:
            print("  |     |     |     |     |     |")
            print(i, end="")
            for x in row:
                print(" | ", end="")
                if x.can_play:
                    print(" ", end="")
                else:
                    print("-", end="")
                if x.colour == -1:
                    print(" ", end="")
                elif x.colour == 0:
                    print("X", end="")
                elif x.colour == 1:
                    print("O", end="")
                if x.can_play:
                    print(" ", end="")
                else:
                    print("-", end="")
            print(" |")
            print("  |_____|_____|_____|_____|_____|")
            i = i - 1
        print("   x=1     2     3     4     5   ")

    def draw_board(self, screen):

        top_left_corner = [244, 244]
        square_length = 100
        gap = 6

        pygame.draw.rect(screen, dark_grey, [top_left_corner[0], top_left_corner[1], len(self.board) * square_length +
                                             gap, len(self.board) * square_length + gap])
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                x = top_left_corner[0] + gap + square_length * i
                y = top_left_corner[1] + gap + square_length * j

                self.board[i][j].collision_rect = [x, y, square_length - gap, square_length - gap]

                if self.board[i][j].can_play:
                    pygame.draw.rect(screen, grey, [x, y, square_length - gap, square_length - gap])
                else:
                    pygame.draw.rect(screen, darker_grey, [x, y, square_length - gap, square_length - gap])
                if self.board[i][j].colour == 0:
                    pygame.draw.circle(screen, dark_grey,
                                       [top_left_corner[0] + gap + int(square_length * (i + 1 / 2)) - 3,
                                        top_left_corner[1] + gap + int(square_length * (j + 1 / 2)) - 3],
                                       38)
                    pygame.draw.circle(screen, white, [top_left_corner[0] + gap + int(square_length * (i + 1 / 2)) - 3,
                                                       top_left_corner[1] + gap + int(square_length * (j + 1 / 2)) - 3],
                                       35)
                elif self.board[i][j].colour == 1:
                    pygame.draw.circle(screen, dark_grey,
                                       [top_left_corner[0] + gap + int(square_length * (i + 1 / 2)) - 3,
                                        top_left_corner[1] + gap + int(square_length * (j + 1 / 2)) - 3],
                                       38)
                    pygame.draw.circle(screen, black, [top_left_corner[0] + gap + int(square_length * (i + 1 / 2) - 3),
                                                       top_left_corner[1] + gap + int(square_length * (j + 1 / 2)) - 3],
                                       35)

    def score(self):
        score_black = 0
        score_white = 0

        for i in range(5):
            for j in range(5):
                if self.board[i][j].colour == 0:
                    score_white += 1
                elif self.board[i][j].colour == 1:
                    score_black += 1

        return [score_white, score_black]

    # calculates winner. 1 = white, -1 = black, 0 = tie
    def winner(self):

        score = self.score()

        if score[0] > score[1]:
            return 1
        elif score[0] < score[1]:
            return -1
        elif score[0] == score[1]:
            return 0

    def obtain_legal_moves(self):

        legal_moves = []

        for row in self.board:
            for x in row:
                for p in self.players[self.turn].piece_set:
                    if x.can_play and p.playable:
                        legal_moves.append((x, p))

        return legal_moves

def make_game():
    game = Game()
    return game
