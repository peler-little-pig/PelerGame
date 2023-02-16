from typing import List
from Data.AllData import *


class TreasureGroup(List):
    def __init__(self):
        super().__init__()

    def draw(self):
        for treasure in self:
            treasure.draw()

    def process(self):
        for treasure in self:
            treasure.process()
