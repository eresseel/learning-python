import os
os.environ["KIVY_NO_CONSOLELOG"] = "1" # a konsole logot kikapcsolja
os.environ["KIVY_HOME"] = os.getcwd() + "/8.configuracio"

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
Builder.load_file('./8.configuracio/kvKodBetoltese.kv')

kv_string = """
<AlapWidget>:
    Button:
        text: "Gomb1"
        size_hint: 0.2, 0.5
        pos_hint: {"top":1}

"""
Builder.load_string(kv_string)

class AlapWidget(FloatLayout):
    pass

class TesztApp(App):
    def build(self):
        return AlapWidget()
    
TesztApp().run()