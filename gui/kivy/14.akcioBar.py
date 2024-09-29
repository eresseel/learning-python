import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/14.configuracio"

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
Builder.load_file('./14.configuracio/akcioBar.kv')

class AlapWidget(FloatLayout):
    pass

class TesztApp(App):
    def build(self):
        return AlapWidget()
    
TesztApp().run()