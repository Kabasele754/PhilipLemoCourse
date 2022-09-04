import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.clock import Clock

from kivy.properties import OptionProperty, StringProperty, DictProperty
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout


Window.size = (350,550)


class ChatBubble(MDBoxLayout):
    '''A chat bubble for the chat screen messages.'''

    profile = DictProperty()
    msg = StringProperty()
    time = StringProperty()
    sender = StringProperty()
    isRead = OptionProperty('waiting', options=['read', 'delivered', 'waiting'])


class DrawerList(ThemableBehavior, MDList):
    pass

class MyFirstAPP(MDApp):
    def build(self):
        return Builder.load_file("main_kv.kv")

    def on_start(self):
        import datetime
        t = datetime.datetime.now().time()
        self.root.time = (t.hour * 60 + t.minute) * 60 + t.second
        Clock.schedule_interval(self._progress_clock, 0)

    def _progress_clock(self, dt):
        self.root.time += dt

if __name__=="__main__":
    MyFirstAPP().run()