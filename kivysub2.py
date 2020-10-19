from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.dropdown  import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition, 
SlideTransition, CardTransition, SwapTransition, 
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)
from kivy.uix.progressbar import ProgressBar
Config.set('graphics', 'window_state', 'maximized')
typ="start"


class FAWindow(Screen):
    global typ
    show="True"
    exp,st,text="","",""
    txt1 = ObjectProperty(None)
    txt2 = ObjectProperty(None)
    def process0(self):
        self.text = self.txt1.text 
        self.exp=self.text
    def process1(self):
        self.text = self.txt2.text 
        self.st=self.text
    def display(self):
        self.show="True"
        if typ=="start":
            if not(self.st.startswith(self.exp)):
                self.show="False"
        elif typ=="end":
            if not(self.st.endswith(self.exp)):
                self.show="False"
        else:
            if self.exp not in self.st:
                self.show="False"
        popup = Popup(title ="Result", content = Label(text=self.show), 
                        size_hint =(None, None), size =(200, 200))
        popup.open()
    def call(self, value):
        if value=='Starts with':
            typ="start"
        elif value=='Ends with':
            typ="end"
        else:
            typ="bet"
        pass
    
    def df(self):
        sm.current="dfa"
    def nf(self):
        sm.current="ndfa"
    
class Ndfa(Screen):
    def active(self):
        sm.current="comm"
    pass
class Dfa(Screen):
    def active(self):
        sm.current="comm"
    pass
class CommonFA(Screen):
    show="True"
    
    exp,st,text="","",""
    txt1 = ObjectProperty(None)
    txt2 = ObjectProperty(None)
    def process0(self):
        self.text = self.txt1.text 
        self.exp=self.text
    def process1(self):
        self.text = self.txt2.text 
        self.st=self.text
    def display(self):
        #dfatrans(txt1,txt2,typ)
        pb = ProgressBar(max=1000)
        popup = Popup(title ="Result", content = Label(text=self.show), 
                        size_hint =(None, None), size =(500, 500))
        popup.open()
    def call(self, value):
        typ=value
        pass
    def back(self):
        sm.current="fai"
    pass

class WindowManager(ScreenManager):
    pass

sm = WindowManager(transition=FadeTransition())
kv = Builder.load_file("Auto2.kv")

screens=[FAWindow(name="fai"), Ndfa(name="ndfa"), Dfa(name="dfa"),CommonFA(name="comm")]


for screen in screens:
    sm.add_widget(screen)
    
sm.current = "fai"

class Kivysub(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Kivysub().run()
