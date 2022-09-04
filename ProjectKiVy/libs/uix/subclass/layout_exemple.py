from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivymd.material_resources import dp

Builder.load_file("libs/uix/kv/layout_exemple.kv")

class WidgetExemple(Widget):
    pass


class BoxLayoutExemple(BoxLayout):
    pass

class AnchorLayoutExemple(AnchorLayout):
    pass

class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


class GridLayoutExemple(GridLayout):
    def enregistre(self):
        # Recuation de valeur
        nom = self.ids.nom.text
        postnom = self.ids.postnom.text
        prenom = self.ids.prenom.text

        # Affichage de valeur dan le label
        self.ids.ecran.text = f"Bonjour je m'appelle {nom} {postnom} {prenom}"

        # effacer les champs
        self.ids.nom.text = ''
        self.ids.postnom.text = ''
        self.ids.prenom.text = ''
