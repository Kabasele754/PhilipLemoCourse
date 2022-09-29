import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import sqlite3
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
Window.size = (350,550)

# ce Tp permet d'ajouter un etudiant dans une base donnée pour esseye
class Enregister(MDApp):

    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database Or Connect To One 
        conn = sqlite3.connect('engister.db')

        # Create A Cursor
        c = conn.cursor()

        # Create a Table 
        c.execute("""CREATE TABLE if not exists etudiants(
    			nom text, postnom text, prenom text, phone text, email text)
    		 """)

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

        return Builder.load_file('main_kv.kv')

    def submit(self):
        nom = self.root.ids.nom.text
        postnom= self.root.ids.postnom.text
        prenom= self.root.ids.prenom.text
        phone= self.root.ids.phone.text
        email= self.root.ids.email.text
        # Create Database Or Connect To One
        conn = sqlite3.connect('engister.db')
        # Create A Cursor
        c = conn.cursor()
        # Add A Record
        sqldb = ("INSERT INTO etudiants VALUES (?,?,?,?,?)")
        mydata = (nom, postnom, prenom, phone, email)
        c.execute(sqldb,mydata)

        # Clear the input box
        self.root.ids.nom.text = ''
        self.root.ids.postnom.text = ''
        self.root.ids.prenom.text = ''
        self.root.ids.phone.text = ''
        self.root.ids.email.text = ''

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

    def select_data(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('engister.db')
        c = conn.cursor()
        c.execute("SELECT * FROM etudiants")
        datas = c.fetchall()
        word = ''

        for data in datas:
            data = f'{word}\n{data[0]}'
            self.root.ids.word_label.text = f'{word}'
            print(data)

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

if __name__ == "__main__":
    Enregister().run()