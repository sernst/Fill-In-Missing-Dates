import cauldron as cd
import random

dates = cd.shared.dates

cd.display.text(
    """
    Then create a list of average temperatures in Minnesota for each of
    these dates:
    """
)

cd.shared.temperatures = [random.randint(-10, 40) for _ in range(len(dates))]

cd.display.listing(cd.shared.temperatures)

