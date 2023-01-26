from typing import List

from Coin.BaseCoin import BaseCoin


class CoinGroup(List[BaseCoin]):
    def __init__(self):
        super().__init__()

    def draw(self):
        for coin in self:
            coin.draw()

    def process(self):
        self.delete()
        for coin in self:
            coin.process()

    def delete(self):
        for i in range(len(self)):
            if self[i].is_should_delete:
                del self[i]
                break
