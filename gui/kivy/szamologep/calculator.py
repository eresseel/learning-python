import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"
os.environ["KIVY_HOME"] = os.getcwd() + "/config"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file('./config/view/calculator.kv')

class CalculatorLayout(BoxLayout):

    clear = False

    def calculate(self):
        expression = self.ids["display"].text

        try:
            exp = str(eval(expression))
        except:
            exp = "Invalid operation"
            self.clear = True

        self.ids["display"].text = exp

    def buttonPressed(self, btn):
        if self.clear:
            self.ids["display"].text = ""
            self.clear = False

        text = btn.text
        self.ids["display"].text += text


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()