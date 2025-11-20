"""
CP1404 Practical - Dynamic Labels
Dynamically create a label for each name in a list.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program that dynamically creates labels."""

    def __init__(self, **kwargs):
        """Construct the app and define the data model."""
        super().__init__(**kwargs)
        self.names = ["Prab", "Lindsay", "Andrew", "Jordan", "Casey"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add it to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()