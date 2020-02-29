import os
os.environ['KIVY_GL_BACKEND']= 'angle_sdl2'
import sys
import logging
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.label import Label
from connected import Connected
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost/TMS')
class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText
        with engine.connect() as conn:
            result = conn.execute("SELECT * FROM users WHERE username='{}' AND password='{}'".format(loginText,passwordText))
            if result.fetchone()!=None:
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'connected'
            else:
                self.error_msg.text='Wrong username or password'
        

        

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
        self.ids['error'].text = ""

class TMSApp(App):
    username = StringProperty("")
    password = StringProperty(None)
    print(username)
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        return manager


if __name__ == '__main__':
    TMSApp().run() 