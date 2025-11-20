"""
CP1404 Practical
UnreliableCar class tests

The point of an UnreliableCar is that it randomly does not always drive.
These tests run several times in order to see that randomness.
We expect the good car (high reliability) to drive more often than the bad car.
"""

from unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""
    # Create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # Attempt to drive the cars many times and show how far they actually drive
    for distance in range(1, 12):
        print(f"Attempting to drive {distance}km:")
        print(f"{good_car.name:12} drove {good_car.drive(distance):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(distance):2}km")

    # Show final states
    print(good_car)
    print(bad_car)


if __name__ == "__main__":
    main()
