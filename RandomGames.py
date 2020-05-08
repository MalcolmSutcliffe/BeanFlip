import Game
import Player
import PlayerRandom
import PlayerHighScore
import PlayerMostSwaps
import PlayerLargestLead
import copy


# p1 = PlayerRandom.make_player(1)
# p2 = PlayerRandom.make_player()
# game = Game.make_game()
#
# for i in range(12):
#     p1.play_move(game)
#     p2.play_move(game)
#
# outcome = game.winner()
# score = game.score()
#
# if outcome == 0:
#     print("Game Over! Tie!" + str(score[1]) + " to " + str(score[0]))
# elif outcome == 1:
#     print("Game Over! White wins " + str(score[0]) + " to " + str(score[1]))
# elif outcome == -1:
#     print("Game Over! Black wins " + str(score[1]) + " to " + str(score[0]))

n = 20

players = [PlayerRandom.make_player(), PlayerHighScore.make_player(),
           PlayerMostSwaps.make_player(), PlayerLargestLead.make_player()]

for p1 in players:
    for p2 in players:
        print(p1.name + " as white vs " + p2.name + " as black for " + str(n) + " Games:")
        p1_wins = 0
        p2_wins = 0
        ties = 0

        for _ in range(n):

            game = Game.make_game()

            for i in range(12):
                p1.play_move(game)
                p2.play_move(game)

            outcome = game.winner()
            score = game.score()

            if outcome == 0:
                # print("Game Over! Tie!" + str(score[1]) + " to " + str(score[0]))
                ties += 1
            elif outcome == 1:
                # print("Game Over! White wins " + str(score[0]) + " to " + str(score[1]))
                p1_wins += 1
            elif outcome == -1:
                # print("Game Over! Black wins " + str(score[1]) + " to " + str(score[0]))
                p2_wins += 1

        print()
        print("Total " + p1.name + " wins as white: " + str(p1_wins))
        print("Total " + p2.name + " wins as black: " + str(p2_wins))
        print("Total ties: " + str(ties))
        print()


