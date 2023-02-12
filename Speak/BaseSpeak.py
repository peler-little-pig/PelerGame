from GUI.Label import *
from GUI.Manager import Manager


class BaseSpeak(Label):
    def __init__(self, actor):
        super().__init__(Manager('./Res/GUI_Theme/Speak/base_speak.json'), actor.left - 300, actor.top - 30,
                         600 + actor.width, 30, '')
        self.actor = actor
        self.last_wait = 0

    def begin_say(self, text, last):
        self.set_text(text)
        self.last_wait = last

    def stop_say(self):
        self.set_text('')

    def process(self):
        if self.last_wait <= 0:
            self.stop_say()
        else:
            self.last_wait -= 1
        self.ui_manager.update(0)
        self.set_position((self.actor.left - 300,self.actor.top - 30))

    def draw(self):
        self.ui_manager.draw()
