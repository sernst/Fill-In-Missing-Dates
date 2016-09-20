from datetime import date
from datetime import timedelta

import cauldron as cd

START_DATE = date(2016, 1, 1)
DAY_COUNT = 15

cd.shared.dates = [START_DATE + timedelta(days=i) for i in range(DAY_COUNT)]

cd.display.markdown(
    """
    # Find Missing Dates

    Start by creating a list of {{ count }} dates from {{ start }} to
    {{ end }}:
    """,
    count=DAY_COUNT,
    start=START_DATE,
    end=START_DATE + timedelta(days=DAY_COUNT)
)

cd.display.listing(cd.shared.dates)




