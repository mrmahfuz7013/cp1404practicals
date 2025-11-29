"""
CP1404 Practical
SilverServiceTaxi class tests
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi functionality."""

    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)

    # Assert correct fare calculation:
    # Base: 1.23 * 2 = 2.46 per km
    # 18 km = 44.28
    # + 4.50 flagfall = 48.78 → rounded to 48.8
    fare = taxi.get_fare()
    print("Fare:", fare)
    assert fare == 48.8, f"Expected 48.8, got {fare}"

    print("SilverServiceTaxi tests passed!")


main()
