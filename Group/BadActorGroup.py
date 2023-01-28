from Lib.Compute.SpaceCompute import *


class BadActorGroup(object):
    def __init__(self):
        super().__init__()
        self.group = {}

    def bad_actors(self):
        bad_actors = []
        for bad_actor_list in self.group.values():
            for bad_actor in bad_actor_list:
                bad_actors.append(bad_actor)
        return bad_actors

    def draw(self):
        for bad_actor in self.bad_actors():
            bad_actor.draw()

    def process(self):
        for key in self.group.keys():
            if self.is_all_dead(self.group[key]):
                key.is_door_open = True
        for bad_actor in self.bad_actors():
            bad_actor.process()

    def is_all_dead(self, bad_actor_list):
        result = True
        for bad_actor in bad_actor_list:
            result = result and (not bad_actor.is_alive())
        return result
