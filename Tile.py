class Tile:

    colour = -1

    def __init__(self, coordinates, colour=-1, can_play=True):

        self.collision_rect = [0, 0, 0, 0]
        self.colour = colour
        self.can_play = can_play
        self.coordinates = coordinates


def make_tile(coordinates, colour=-1, can_play=True):
    tile = Tile(coordinates, colour, can_play)
    return tile
