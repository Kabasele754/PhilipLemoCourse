from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField

from model.database_etu import Database


Builder.load_file("libs/uix/kv/screen_data.kv")
db = Database('database_student.db')

class TabData(FloatLayout, MDTabsBase):
    pass
class TabDataEtudiant(FloatLayout, MDTabsBase):
    pass
class GridDataTabeEtudiant(MDBoxLayout):
    name = StringProperty()
    lastname = StringProperty()
    firstname = StringProperty()
    age = StringProperty()
    def __init__(self, **kwargs):
        super(GridDataTabeEtudiant, self).__init__(**kwargs)
        self.data_tables =  MDDataTable(
                column_data=
                    [
                    ("Id", dp(10)),
                    ("Nom", dp(15)),
                    ("PostNom", dp(15)),
                    ("PreNom", dp(15)),
                    ("Age", dp(15)),
                    ],
            row_data=[
                (
                    "1",
                    "Mwenze",
                    "Kankonde",
                    "Merveille",
                    "23 ans"
                ),],
            pos_hint={'center_x': .5, 'center_y': .62},
            use_pagination=True,
            rows_num=5,
            #check=True,
        )
        self.data_tables.row_data = self.get_all_data()
        #self.data_tables.bind(on_row_press=self.row_selected)
        self.add_widget(self.data_tables)

    def get_all_data(self):
        data = []
        for row in db.fetch_all():
            data.append(row)
        return data

    def row_selected(self, table, row):
        # get start index from selected row item range
        start_index, end_index = row.table.recycle_data[row.index]["range"]

        # populate form with selected record
        self.populate_form(row.table.recycle_data[start_index]["text"])

    def clear_form(self, name, lastname, firstname, age):
        name = ''
        lastname = ''
        firstname = ''
        age = ''
    def populate_form(self, row_id):
        # retrieve row data from db using record_id
        # returned dataset tuple: (record_id, matter_name, file_name, description, location)
        row_data = db.get_record_by_id(row_id)

        self.ids.student_id.text = str(row_data[0])
        self.root.ids.name.text = row_data[1]
        self.root.ids.lastname.text = row_data[2]
        self.root.ids.firstname.text = row_data[3]
        self.root.ids.age.text = row_data[4]

    def sava_data(self, id, name, lastname, firstname, age):
        id.text = ''
        if name.text == '' or lastname.text == '' or firstname.text == '' or age.text == '':
            id.text = 'Veuillez remplir tous les champs'
        else:
            name = name.text
            lastname = lastname.text
            firstname = firstname.text
            age = age.text
            db.insert(name, lastname, firstname, age)
            self.data_tables.row_data = self.get_all_data()
            self.clear_form(name, lastname, firstname, age)

class ContentDialog(BoxLayout):
    pass

class GridDataTabeEnseignant(MDBoxLayout):
    def __init__(self, **kwargs):
        super(GridDataTabeEnseignant, self).__init__(**kwargs)
        self.data_tables = MDDataTable(
            column_data=
            [
                ("Id", dp(20)),
                ("Nom", dp(15)),
                ("PostNom", dp(15)),
                ("PreNom", dp(15)),
                ("Age", dp(15)),
            ],
            row_data=[
                (
                    "1",
                    "Mwenze",
                    "Kankonde",
                    "Merveille",
                    "23 ans"
                ), ],
            pos_hint={'center_x': .5, 'center_y': .70},
            size_hint=(1, .9),
            use_pagination=True,
            rows_num=5,
            check=True,
        )
        self.data_tables.row_data = self.get_all_data()
        self.add_widget(self.data_tables)

    def get_all_data(self):
        data = []
        for row in db.fetch_all():
            data.append(row)
        return data



class ScreenData(Screen):
    dialog = None
    def __init__(self, **kwargs):
        super(ScreenData, self).__init__(**kwargs)
        self.data_tables = MDDataTable(
            column_data=
            [
                ("Id", dp(20)),
                ("Nom", dp(15)),
                ("PostNom", dp(15)),
                ("PreNom", dp(15)),
                ("Age", dp(15)),
            ],
            row_data=[
                (
                    "1",
                    "Mwenze",
                    "Kankonde",
                    "Merveille",
                    "23 ans"
                ), ],
            pos_hint={'center_x': .5, 'center_y': .70},
            size_hint=(1, .9),
            use_pagination=True,
            rows_num=8,
            check=True,
        )
        self.data_tables.row_data = self.get_all_data()
        #self.add_widget(self.data_tables)

    def get_all_data(self):
        data = []
        for row in db.fetch_all():
            data.append(row)
        return data

    def clear_form(self):
        self.name_int.text = ''
        self.lastname_int.text = ''
        self.firstname_int.text = ''
        self.age_int.text = ''
        #self.root.ids.age.text = ''

    def show_confirmation_dialog(self, obj):

        def close_dilog(obj):
            self.dialog.dismiss()
        def use_input(obj):
            print('heare i wan to print the Todo and time', self.firstname_int.text)
            self.id_label.text = ''
            if self.name_int.text == '' or self.lastname_int.text == '' or self.firstname_int.text == '' or self.age_int.text == '':
                self.id_label.text = 'Veuillez remplir tous les champs'
            else:
                name = self.name_int.text
                lastname = self.lastname_int.text
                firstname = self.firstname_int.text
                age = self.age_int.text
                db.insert(name, lastname, firstname, age)
                self.data_tables.row_data = self.get_all_data()
                self.clear_form()

        main_box = BoxLayout(orientation="vertical", spacing="12dp", size_hint_y=None,
                  height=dp("160"))
        second_box= MDGridLayout(  # GridLayout des input text
        cols= 2,
        spacing= 30,
        padding= dp(10))
        # Partie input
        self.name_int = MDTextField(mode= "rectangle",hint_text= "Name")
        self.id_label = MDLabel(text= '',color= (1, 0, 0, 1))
        self.lastname_int = MDTextField(mode= "rectangle",hint_text= "Lastname")
        self.firstname_int = MDTextField(mode= "rectangle",hint_text= "Firstname")
        self.age_int = MDTextField(mode= "rectangle",hint_text= "Age")

        second_box.add_widget(self.name_int)
        second_box.add_widget(self.lastname_int)
        second_box.add_widget(self.firstname_int)
        second_box.add_widget(self.age_int)
        second_box.add_widget(self.id_label)
        main_box.add_widget(second_box)

        if not self.dialog:
            self.dialog = MDDialog(
                title="Ajouter Enseignat :",
                type="custom",
                content_cls= main_box,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        #text_color=self.theme_cls.primary_color,
                        text_color= '#3492eb',
                        on_press=close_dilog
                    ),
                    MDFlatButton(
                        text="VALID",
                        theme_text_color="Custom",
                        text_color='#3492eb',
                        #text_color=self.theme_cls.primary_color,
                        on_press=use_input
                    ),
                ],
            )
        self.dialog.open()



