import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/15.configuracio"

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
Builder.load_file('./15.configuracio/vaszon.kv')
from kivy.graphics import Rectangle, Color, Ellipse

class AlapWidget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Color(1,0,0,1)
            Rectangle(pos=(200,200), size=(150,50))
            Color(0,1,0,1)
            Ellipse(pos=(200,200), size=(150,50))
            Color(1,1,1,1)
            Rectangle(source="./15.configuracio/image/Jack.jpg")

class TesztApp(App):
    def build(self):
        return AlapWidget()
    
TesztApp().run()