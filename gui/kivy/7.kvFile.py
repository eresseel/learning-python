import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/7.configuracio"

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class AlapWidget(FloatLayout):
    pass

class KvFileApp(App):
    def build(self):
        return AlapWidget()
    
KvFileApp().run()