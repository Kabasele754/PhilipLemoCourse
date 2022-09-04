from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder

Builder.load_file("libs/uix/kv/widgeet_exemple.kv")


class WidgetExempleSecond(GridLayout):
    mon_text_lab = StringProperty("1")
    compteur = 1
    compteur_actif = False
    mon_text_slider = StringProperty("Valeur")

    def cliquer(self):
        print("Button cliquer")
        if self.compteur_actif:
            self.compteur += 1
            self.mon_text_lab = str(self.compteur)

    def on_toggle(self, widget):
        # print("Toggle", widget.state)

        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True

    def on_switch(self, widget):
        print("VAleur Switch :", widget.active)

    def on_slider_value(self, widget):
        print(widget.value)
        self.mon_text_slider = str(int(widget.value))

