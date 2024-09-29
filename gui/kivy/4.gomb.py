import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/4.configuracio"

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class AlapWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gomb1 = Button(text="Gomb1", size=(100,50), pos=(0,0), id="gomb1")
        gomb1.bind(on_press=self.helloGomb)
        self.add_widget(gomb1)

        gomb2 = Button(text="Gomb2", size=(100,50), pos=(100,100), id="gomb2")
        gomb2.bind(on_press=self.helloGomb)
        self.add_widget(gomb2)

    def helloGomb(self, instance):
        if instance.id == "gomb1":
            print("Hello Gomb1")
        elif instance.id == "gomb2":
            print("Hello Gomb2")

class TesztApp(App):
    def build(self):
        return AlapWidget()
    
TesztApp().run()