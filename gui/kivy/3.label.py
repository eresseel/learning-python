import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/4.configuracio"

from kivy.app import App
from kivy.uix.label import Label

class TesztApp(App):
    def build(self):
        return Label(text="[color=ff0000]Hello[/color] [color=00ff00]World![/color]", font_size=60, 
                     italic=True, underline=True, color=(1, 0.5, 0, 1), bold=True, font_name="./3.configuracio/fonts/Montserrat-Bold.ttf",
                     markup=True)
    
TesztApp().run()