import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/2.configuracio"

from kivy.config import Config
# lokalis konfiguracios allomany 
# /home/kerb3rosz/.kivy/config.ini 
# itt globalis beallitasok vannak
Config.set("graphics", "width", "1366")
Config.set("graphics", "height", "768")
Config.set("graphics", "resizable", "1") #ablak nem meretezheto at
Config.set("graphics", "borderless", "0") #ablak kerete nem  jelenik meg ha 1 az ertek
Config.write() #elmenti a config.ini fileba, nem ajanlot a hasznalata

from kivy.app import App
from kivy.uix.widget import Widget

class TesztApp(App):
    def build(self):
        return Widget()
    
TesztApp().run()