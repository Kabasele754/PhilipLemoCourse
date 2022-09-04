import os


os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ObjectProperty
from libs.uix.subclass.navigation_creen_manager import NavigationScreenManager



class MyScreenManager(NavigationScreenManager):
    pass


class FirstApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


FirstApp().run()
