from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivyx.uix.analogclock import KXAnalogClock
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("libs/uix/kv/screen_clock_anologic.kv")

class ScreenClockAnalog(KXAnalogClock):
    def __init__(self, **kwargs):
        super(ScreenClockAnalog, self).__init__(**kwargs)

    def on_start(self):
        import datetime
        t = datetime.datetime.now().time()
        self.root.time = (t.hour * 60 + t.minute) * 60 + t.second
        Clock.schedule_interval(self._progress_clock, 0)

    def _progress_clock(self, dt):
        self.root.time += dt
