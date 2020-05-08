from Player import Player
import random


class PlayerRandom(Player):

    def __init__(self, colour=-1, name="Random"):
        super().__init__(colour, name)

    def play_move(self, game):

        # if game.turn != self.colour:
        #     return

        legal_squares = []
        legal_pieces = []

        for row in game.board:
            for x in row:
                if x.can_play:
                    legal_squares.append(x)

        for p in game.players[game.turn].piece_set:
            if p.playable:
                legal_pieces.append(p)

        if len(legal_squares) == 0 or len(legal_pieces) == 0:
            return

        random_square = random.choice(legal_squares)

        random_piece = random.choice(legal_pieces)

        game.play(random_square.coordinates, random_piece.piece_type)


def make_player(colour=-1, name="Random"):
    player = PlayerRandom(colour, name)
    return player
