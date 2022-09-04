import sqlite3

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem

Builder.load_file("libs/uix/kv/screen_home.kv")
class Content(BoxLayout):
    pass
class DonneEtudianList(OneLineIconListItem):
    pass
class ScreenHome(Screen):
    """ L'ecran home """
    def show_confirmation_dialog(self, obj):
        def close_dilog(obj):
            self.dialog.dismiss()

        def use_input(obj):
            print('heare i wan to print the Todo and time')

        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=close_dilog
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=use_input
                    ),
                ],
            )
        self.dialog.open()
    def rechercher(self,r,t):
        r.data = []
        con = sqlite3.connect("model/engister.db")
        curseur = con.cursor()
        curseur.execute("SELECT * FROM etudiants")
        donnees = curseur.fetchall()

        for donnee in donnees:
            if t in str(donnee):
                r.data.append(
                    {
                        'viewclass': "DonneEtudianList",
                        'markup': True,
                        'text': " trouver: " + f"{str(donnee[1]).lower()} {str(donnee[2])} {str(donnee[3])}"
                    }
                )





