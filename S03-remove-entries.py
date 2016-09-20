import cauldron as cd
import pandas as pd

# These are the indexes we're going to make missing from our data set
REMOVE_INDEXES = (14, 9, 8, 3, 0)

# Create copies of the dates and temperatures so we don't corrupt their
# original values
dates = cd.shared.dates.copy()
temperatures = cd.shared.temperatures.copy()

cd.display.text(
    """
    Now we're going to remove a few entries from the dates and temperatures
    lists. These will be the missing dates that we try to find:
    """
)

# Remove the entries by index
missing = zip(
    [dates.pop(i) for i in REMOVE_INDEXES],
    [temperatures.pop(i) for i in REMOVE_INDEXES]
)
cd.display.listing(['{}: {}&deg;'.format(d, t) for d, t in missing])

cd.display.text(
    """
    Make a data frame of the remaining dates and temperatures. This is the
    source data we'll use have to fill in rows for the dates we made missing:
    """
)

cd.shared.df = pd.DataFrame(dict(
    date=dates,
    temperature=temperatures
))

cd.display.table(cd.shared.df)
