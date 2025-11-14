"""
CP1404 Practical
Kivy GUI program to square a number.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """Kivy App for squaring a number."""

    def build(self):
        """
        Build the Kivy app from the kv file.

        Returns:
            The root widget loaded from the KV layout.
        """
        Window.size = (300, 150)
        self.title = "Square Number 2"
        self.root = Builder.load_file("squaring.kv")
        return self.root

    def handle_calculate(self, value):
        """
        Handle calculation when the Square button is pressed.

        Args:
            value (str): The text from the input_number field.

        Updates:
            output_label text to the squared value, or clears it for invalid input.
        """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = f"{result}"
        except ValueError:
            self.root.ids.output_label.text = ""


SquareNumberApp().run()
