# Gantt charting
# AUTHOR Sven Schrodt
# SINCE 20250708

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt

mpl.use("TkAgg")  # Workaround for MacOS Bug with ⌘+Q - use new backend


df = pd.DataFrame(
    {
        "task": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
        "team": [
            "R&D",
            "Accounting",
            "Sales",
            "Sales",
            "IT",
            "R&D",
            "IT",
            "Sales",
            "Accounting",
            "Accounting",
            "Sales",
            "IT",
        ],
        "start": pd.to_datetime(
            [
                "20 Oct 2022",
                "24 Oct 2022",
                "26 Oct 2022",
                "31 Oct 2022",
                "3 Nov 2022",
                "7 Nov 2022",
                "10 Nov 2022",
                "14 Nov 2022",
                "18 Nov 2022",
                "23 Nov 2022",
                "28 Nov 2022",
                "30 Nov 2022",
            ]
        ),
        "end": pd.to_datetime(
            [
                "31 Oct 2022",
                "28 Oct 2022",
                "31 Oct 2022",
                "8 Nov 2022",
                "9 Nov 2022",
                "18 Nov 2022",
                "17 Nov 2022",
                "22 Nov 2022",
                "23 Nov 2022",
                "1 Dec 2022",
                "5 Dec 2022",
                "5 Dec 2022",
            ]
        ),
        "completion_frac": [1, 1, 1, 1, 1, 0.95, 0.7, 0.35, 0.1, 0, 0, 0],
    }
)

df['days_to_start'] = (df['start'] - df['start'].min()).dt.days

df['days_to_end'] = (df['end'] - df['start'].min()).dt.days

df['task_duration'] = df['days_to_end'] - df['days_to_start'] + 1  # to include also the end date

df['completion_days'] = df['completion_frac'] * df['task_duration']



print(df.head())
plt.barh(y=df['task'], width=df['task_duration'], left=df['days_to_start'])
plt.show()