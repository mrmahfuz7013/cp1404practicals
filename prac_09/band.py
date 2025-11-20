"""
CP1404 Practical
Band class
"""


class Band:
    """Band has a name and a collection of Musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of the Band."""
        # Format: BandName (Musician1, Musician2, Musician3)
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return each musician's play() result on separate lines."""
        return "\n".join(musician.play() for musician in self.musicians)
