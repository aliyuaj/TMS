import os
os.environ['KIVY_GL_BACKEND']= 'angle_sdl2'
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Connected(Screen):
    def dashboard_clicked(self,option):
        if option=='Logout':
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'login'
            self.manager.get_screen('login').resetForm() 
        elif option=='Students':
            self.ids['content'].add_widget(Builder.load_file('students.kv'))
            
   