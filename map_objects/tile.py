class Tile:
    """
    a tile on a map. may or may not be blocked, may or may not block sight
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # default = if a tile is blocked, then it blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

        self.explored = False
