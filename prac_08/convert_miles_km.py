"""
CP1404 Practical-08
Miles to Kilometres Converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934

class MilesToKilometresApp(App):
    """App to convert miles to kilometres."""

    def build(self):
        """Build kivy app from kv file."""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        """Convert miles to kilometres."""
        try:
            result = float(value) * MILES_TO_KM
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, value, change):
        """Increases input number by 1"""
        try:
            number = int(value)
        except ValueError:
            number = 0 # If box is invalid

        number += change

        self.root.ids.input_number.text = str(number)



MilesToKilometresApp().run()
