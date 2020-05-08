from Player import Player
import random
import copy


class PLayerLargestLead(Player):

    def __init__(self, colour=-1, name="LargestLead"):
        super().__init__(colour, name)

    def play_move(self, game):

        # if game.turn != self.colour:
        #     return

        legal_moves = game.obtain_legal_moves()
        high_score = -50
        best_moves = []

        d = {}

        for m in legal_moves:
            vg = copy.deepcopy(game)
            vg.play(m[0].coordinates, m[1].piece_type)
            new_score = vg.score()[game.turn] - vg.score()[1-game.turn]
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


def make_player(colour=-1, name="LargestLead"):
    player = PLayerLargestLead(colour, name)
    return player
