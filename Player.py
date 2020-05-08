import Piece
import pygame

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
dark_grey = (64, 64, 64)
light_grey = (196, 196, 196)


class Player:

    def __init__(self, colour=-1, name="unnamed"):
        self.piece_set = [Piece.make_piece(i + 1, True) for i in range(12)]
        self.colour = colour
        self.name = name

    def print_piece_set(self):

        for row in range(3):
            print(" ", end="")
            for i in self.piece_set:
                if i.playable:
                    j = 0
                    for x in i.swap_grid[row]:
                        if x:
                            print("o", end="_")
                        elif row < 2:
                            print("_", end="_")
                        else:
                            print("_", end="_")
                        if j < 2:
                            print("|", end="")
                        else:
                            print(" ", end="")
                        j += 1
                print(" ", end="")
            print()

    def draw_pieces(self, screen):

        square_length = 20
        gap = 2

        top_left_corner = [264, 74]

        if self.colour == 1:
            top_left_corner = [264, 780]

        draw_colour = white

        if self.colour == 1:
            draw_colour = black

        for i in range(len(self.piece_set)):
            if self.piece_set[i].playable:

                h = i
                d = 0

                if i > 5:
                    h = i - 6
                    d = 1

                x = top_left_corner[0] + (len(self.piece_set[i].swap_grid) + 1) * h * square_length
                y = top_left_corner[1] + (len(self.piece_set[i].swap_grid) + 1) * d * square_length

                self.piece_set[i].draw_piece(screen, x, y, draw_colour)


def make_player(colour=-1, name="unnamed"):
    player = Player(colour, name)
    return player
