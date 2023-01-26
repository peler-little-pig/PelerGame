from typing import List


class CoinGroup(List):
    def __init__(self):
        super().__init__()

    def draw(self):
        for coin in self:
            coin.draw()

    def process(self):
        for coin in self:
            coin.process()