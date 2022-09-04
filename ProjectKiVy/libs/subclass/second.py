import os

from kivy.metrics import dp
from kivy.uix.button import Button

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView


class ScrollViewExemple(ScrollView):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super(StackLayoutExemple, self).__init__(**kwargs)
        for i in range(100):
            b = Button(
                text=str(i + 1),
                size_hint=(None, None),
                size=(dp(100), dp(100))
            )
            self.add_widget(b)


class SecondApp(App):
    pass


if __name__ == "__main__":
    SecondApp().run()
