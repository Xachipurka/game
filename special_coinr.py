from coin import Coin
import player

class Special_coinr(Coin):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255, 0, 0)

    def collect(self):
        self.col = False
#        player.xs += 10
