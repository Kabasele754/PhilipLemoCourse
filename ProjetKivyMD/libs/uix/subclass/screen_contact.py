import os

from kivy.uix.scrollview import ScrollView
from kivymd import images_path
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
Builder.load_file("libs/uix/kv/screen_contact.kv")


class Content(MDBoxLayout):
    '''Custom content.'''

class ScreenContact(MDScreen, ScrollView, MDGridLayout):

    def on_start(self):
        for i in range(10):
            self.add_widget(
                MDExpansionPanel(
                    icon=os.path.join(images_path, "logo", "kivymd-icon-128.png"),
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    )
                )
            )

