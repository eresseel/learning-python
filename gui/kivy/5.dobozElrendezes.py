import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/5.configuracio"

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class AlapWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 50
        self.padding = 20
    
        gomb1 = Button(text="Gomb1", id="gomb1", size_hint=(0.2, 0.5))
        gomb1.bind(on_press=self.helloGomb)
        self.add_widget(gomb1)

        gomb2 = Button(text="Gomb2", id="gomb2", size_hint=(0.2, 0.5))
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