# Followed https://kivy.org/docs/guide/basic.html#quickstart
import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput

kivy.require('1.10.0')
Config.set('graphics', 'window_state', 'maximized')


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class HexApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    HexApp().run()
