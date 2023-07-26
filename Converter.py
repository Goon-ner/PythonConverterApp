from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder

Config.set('kivy', 'keyboard_mode', 'systemanddock')

Window.size = (360, 640)

class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0

        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number * 1440)
        self.label_seconds.text = str(number * 86400)


class ConverterApp(MDApp):
    def __init__(self, **kwargs):
        self.title = 'Converter'
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Container()



ConverterApp().run()
