from GUI.Label import *


class BaseSpeak(Label):
    def __init__(self, actor):
        super().__init__(actor.left, actor.top - 30, 500, 30, '')
        self.last_WAIT = 0
        self.last_wait = 0
        self.text_vert_alignment = 'left'

    def begin_say(self, text, last):
        self.set_text(text)
        self.last_WAIT = last
        self.last_wait = last

    def stop_say(self):
        self.set_text('')

    def process(self):
        if self.last_wait == 0:
            self.stop_say()
        else:
            self.last_wait -= 1
