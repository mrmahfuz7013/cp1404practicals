"""
CP1404 Practical
Kivy GUI program demonstrating BoxLayout, button events,
text input handling, and dynamic label updates.
"""

from kivy.app import App
from kivy.lang import Builder

KV_FILE = "box_layout.kv"


class BoxLayoutDemo(App):
    """Box Layout Demo app."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file(KV_FILE)
        return self.root

    def handle_greet(self):
        """Handle pressing the Greet button."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Handle pressing the Clear button."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
