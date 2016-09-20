import cauldron as cd
import pandas as pd
import datetime
import numpy as np

df = cd.shared.df_modified  # type: pd.DataFrame

cd.display.text(
    """
    Now we want to find any missing entries in the middle and fill them
    in. To do that we're going to check the difference between dates.
    We take each date and subtract it from the previous one. The timedelta
    object that is created should have a value of 1 day unless there is a
    date missing.
    """
)

dates = df['date'].values

for index in range(1, len(dates)):
    today = dates[index]
    yesterday = dates[index - 1]
    days_missing = (today - yesterday).days - 1

    if days_missing < 1:
        # No missing dates here so move on
        continue

    for i in range(days_missing):
        # Add an entry for each missing date

        new_date = yesterday + datetime.timedelta(days=i + 1)
        df = df.append(
            {'date': new_date, 'temperature': np.nan},
            ignore_index=True
        )

        cd.display.text('ADDED: {}'.format(new_date))

cd.display.text(
    """
    Now we have filled in all of the dates missing in the middle of our
    block of dates and the final data frame looks like this:
    """
)

cd.display.table(df.sort_values(by='date'))
