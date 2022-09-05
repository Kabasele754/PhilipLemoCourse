import os
import re
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

#Builder.load_file('./calculator.kv')
Window.size = (350,550)

class CalculatorWidget(Widget):
    # pour initialise to zero
    def effacer(self):
        self.ids.input_screen.text = '0'
    # pour connect the button get value

    def button_value(self, number):
        prev_number = self.ids.input_screen.text

        # pour initilise value button for division by zero
        if "ERREUR" in prev_number:
            prev_number = ''

        # condition for write a number
        if prev_number == '0':
            self.ids.input_screen.text = ''
            self.ids.input_screen.text = f'{number}'
        else:
            self.ids.input_screen.text = f'{prev_number}{number}'
    # pour connect the button get sign

    def operators(self, sign):
        prev_number = self.ids.input_screen.text
        self.ids.input_screen.text = f'{prev_number}{sign}'
    # pour supprimer last caracteur

    def remove_last(self):
        prev_number = self.ids.input_screen.text
        number_mo = prev_number[:-1]
        # show this prev_number on screen
        self.ids.input_screen.text = number_mo
    # pour the results function

    def results(self):
        prev_number = self.ids.input_screen.text

        # can show this result in screen et caste for division bar zero
        try:
            result = eval(prev_number)
            self.ids.input_screen.text = str(result)

        except ZeroDivisionError:
            self.ids.input_screen.text = "ERREUR"
    def positive_negative(self):
        prev_number = self.ids.input_screen.text

        if '-' in prev_number:
            self.ids.input_screen.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_screen.text = f'-{prev_number}'

    def dot(self):
        prev_number = self.ids.input_screen.text
        #num_list_op = prev_number.split("+")
        # il faut add \ pour operator + *
        num_list_op = int(re.split("\+\*-%"))

        # if '+' in prev_number and '.' not in num_list_op[-1]:
        if ('+' in prev_number or '*' in prev_number or '-' in prev_number or '/' in prev_number or '%' in prev_number) \
                and '.' not in num_list_op[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_screen.text = prev_number

        if '.' in prev_number:
            pass
        else:
            prev_number = f"{prev_number}."
            self.ids.input_screen.text = prev_number

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == '__main__':
    CalculatorApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
