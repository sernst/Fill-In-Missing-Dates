import cauldron as cd
import datetime
import pandas as pd
import numpy as np

df = cd.shared.df  # type: pd.DataFrame

cd.display.text(
    """
    First we want to check to see if the first or last entries are missing.
    If either or both of them are, we want to add those entries and mark them
    missing by setting the temperature values to NaN.
    """
)

start_date = datetime.date(2016, 1, 1)

if df['date'].min() > start_date:
    df = df.append(
        {'date': start_date, 'temperature': np.nan},
        ignore_index=True
    )

end_date = datetime.date(2016, 1, 15)

if df['date'].max() < end_date:
    df = df.append(
        {'date': end_date, 'temperature': np.nan},
        ignore_index=True
    )

df = df.sort_values(by='date')

cd.display.text(
    """
    Now our data frame is sure to have entries for the beginning and end dates.
    Here's what it looks like:
    """
)

cd.display.table(df)

cd.shared.df_modified = df
