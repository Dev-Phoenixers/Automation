from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

import os

class MainWindow(Screen):
    def tur(self):
        sm.current="tur"
    def auto(self):
        sm.current="auto"
    def reg(self):
        sm.current="regex"
class AutomataWindow(Screen):
    def dfa(self):
        os.system("python kivysub.py")
    def nfa(self):
        os.system("python kivysub.py")
    def reset(self):
        sm.current="main"

class Regularex(Screen):
    def calculate(self):
        pass
    def reset(self):
        sm.current="main"
class TuringWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")
sm = WindowManager()


screens = [MainWindow(name="main"), AutomataWindow(name="auto"), Regularex(name="regex"), TuringWindow(name="tur")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class Kivymain(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Kivymain().run()
