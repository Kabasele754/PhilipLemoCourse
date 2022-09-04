from kivy.uix.screenmanager import ScreenManager


class NavigationScreenManager(ScreenManager):
    screen_stack = [] #

    # Methode push
    def push(self, nom_screen):
        # Ici on empile les ecrans avec methode append
        self.screen_stack.append(self.current)
        self.transition.direction = 'left'
        self.current = nom_screen

    # Methode pop
    def pop(self):
        nom_creen = self.screen_stack[-1]
        del self.screen_stack[-1]
        self.transition.direction = 'right'
        self.current = nom_creen