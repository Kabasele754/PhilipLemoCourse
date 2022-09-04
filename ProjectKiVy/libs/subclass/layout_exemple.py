from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file("libs/uix/kv/layout_exemple.kv")

class WidgetExemple(Widget):
    pass


class BoxLayoutExemple(BoxLayout):
    pass


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
