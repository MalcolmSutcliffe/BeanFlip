import pygame

white = (255, 255, 255)
highlighted = (255, 253, 200)
black = (0, 0, 0)
grey = (128, 128, 128)
dark_grey = (64, 64, 64)
darker_grey = (80, 80, 80)
light_grey = (196, 196, 196)


class Piece:
    swap_grid = []
    playable = True
    is_selected = False
    piece_type = 0
    collision_rect = [0, 0, 0, 0]

    def __init__(self, piece_type=1, playable=True):

        self.piece_type = piece_type

        self.is_selected = False

        self.collision_rect = [0, 0, 0, 0]

        self.playable = playable

        if piece_type == 1:
            self.swap_grid = [
                [False, False, False],
                [False, True, False],
                [False, False, False],
            ]
        elif piece_type == 2:
            self.swap_grid = [
                [False, False, False],
                [True, False, True],
                [False, False, False],
            ]
        elif piece_type == 3:
            self.swap_grid = [
                [False, True, False],
                [False, False, False],
                [False, True, False],
            ]
        elif piece_type == 4:
            self.swap_grid = [
                [False, False, True],
                [False, True, False],
                [True, False, False],
            ]
        elif piece_type == 5:
            self.swap_grid = [
                [True, False, False],
                [False, True, False],
                [False, False, True],
            ]
        elif piece_type == 6:
            self.swap_grid = [
                [False, False, False],
                [True, True, True],
                [False, False, False],
            ]
        elif piece_type == 7:
            self.swap_grid = [
                [False, True, False],
                [False, True, False],
                [False, True, False],
            ]
        elif piece_type == 8:
            self.swap_grid = [
                [False, True, False],
                [True, False, True],
                [False, True, False],
            ]
        elif piece_type == 9:
            self.swap_grid = [
                [True, False, True],
                [False, False, False],
                [True, False, True],
            ]
        elif piece_type == 10:
            self.swap_grid = [
                [False, True, False],
                [True, True, True],
                [False, True, False],
            ]
        elif piece_type == 11:
            self.swap_grid = [
                [True, False, True],
                [False, True, False],
                [True, False, True],
            ]
        elif piece_type == 12:
            self.swap_grid = [
                [True, True, True],
                [True, False, True],
                [True, True, True],
            ]

    def print_piece(self):
        print("-" * 3)
        for row in self.swap_grid:
            print("|", end="")
            for x in row:
                if x:
                    print("o", end="")
                else:
                    print(" ", end="")
            print("|")
        print("-" * 3)

    def draw_piece(self, screen, x, y, draw_colour):

        square_length = 20
        gap = 2

        if self.is_selected:
            pygame.draw.rect(screen, black, [x, y, len(self.swap_grid) * square_length + gap,
                                             len(self.swap_grid) * square_length + gap])
            pygame.draw.rect(screen, grey, [x + gap, y + gap, len(self.swap_grid) * square_length - gap,
                                            len(self.swap_grid) * square_length - gap])

        else:
            pygame.draw.rect(screen, grey, [x, y, len(self.swap_grid) * square_length + gap,
                                            len(self.swap_grid) * square_length + gap])

        for j in range(len(self.swap_grid)):
            for k in range(len(self.swap_grid[j])):
                if self.swap_grid[j][k]:
                    pygame.draw.rect(screen, draw_colour,
                                     [x + square_length * j + gap,
                                      y + square_length * k + gap,
                                      square_length - gap, square_length - gap])

        self.collision_rect = [x, y, len(self.swap_grid) * square_length, len(self.swap_grid) * square_length]


def make_piece(piece_type=1, playable=True):
    piece = Piece(piece_type, playable)
    return piece
