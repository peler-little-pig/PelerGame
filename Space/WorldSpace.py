from Space.RoomSpace.BadActorRoomSpace import *
from Data.AllData import *

class WorldSpace(BaseSpace):
    def __init__(self, name):
        super().__init__(name)
        self.area_list: List[BaseSpace] = []

    def draw(self):
        for area in self.area_list:
            area.draw()

    def active_area(self):
        for area in self.area_list:
            if area.is_in_this_space():
                return area

    def can_move_up(self):
        return self.active_area().can_move_up()

    def can_move_down(self):
        return self.active_area().can_move_down()

    def can_move_left(self):
        return self.active_area().can_move_left()

    def can_move_right(self):
        return self.active_area().can_move_right()

    def move_up(self):
        if self.can_move_up():
            for area in self.area_list:
                area.move_up()
            return True
        else:
            return False

    def move_down(self):
        if self.can_move_down():
            for area in self.area_list:
                area.move_down()
            return True
        else:
            return False

    def move_left(self):
        if self.can_move_left():
            for area in self.area_list:
                area.move_left()
            return True
        else:
            return False

    def move_right(self):
        if self.can_move_right():
            for area in self.area_list:
                area.move_right()
            return True
        else:
            return False

    def search(self, name: str):
        for area in self.area_list:
            if area.name == name:
                return area

    def process(self):
        for area in self.area_list:
            area.process()

        EventData.is_move_up = False
        EventData.is_move_down = False
        EventData.is_move_left = False
        EventData.is_move_right = False
        if EventData.is_key_w_down:
            EventData.is_move_up = self.move_up()
        if EventData.is_key_s_down:
            EventData.is_move_down = self.move_down()
        if EventData.is_key_a_down:
            EventData.is_move_left = self.move_left()
        if EventData.is_key_d_down:
            EventData.is_move_right = self.move_right()