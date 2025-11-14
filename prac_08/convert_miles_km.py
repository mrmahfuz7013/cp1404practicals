"""
CP1404 Practical
Dynamic Kivy Labels Demo
Create labels dynamically from a list of names.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app that dynamically creates labels for a list of names."""

    def __init__(self, **kwargs):
        """Store data (the names list)."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

    def build(self):
        """
        Build the Kivy GUI from the kv file and
        dynamically create a Label for each name.
        """
        self.title = "Dynamic Labels"
        root = Builder.load_file("dynamic_labels.kv")

        # Add a Label for each name in the list
        for name in self.names:
            temp_label = Label(text=name, font_size=24)
            root.ids.main.add_widget(temp_label)

        return root


DynamicLabelsApp().run()
