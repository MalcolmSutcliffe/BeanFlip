from Player import Player
import random
import copy


class PLayerHighScore(Player):

    def __init__(self, colour=-1, name="HighScore"):
        super().__init__(colour, name)

    def play_move(self, game):

        # if game.turn != self.colour:
        #     return

        legal_moves = game.obtain_legal_moves()
        high_score = 0
        best_moves = []

        d = {}

        for m in legal_moves:
            vg = copy.deepcopy(game)
            vg.play(m[0].coordinates, m[1].piece_type)
            new_score = vg.score()[game.turn]
            d[m] = new_score
            if new_score > high_score:
                high_score = new_score

        for m in legal_moves:
            if d[m] == high_score:
                best_moves.append(m)

        if len(best_moves) == 0:
            return

        move = random.choice(best_moves)

        game.play(move[0].coordinates, move[1].piece_type)


def make_player(colour=-1, name="HighScore"):
    player = PLayerHighScore(colour, name)
    return player
