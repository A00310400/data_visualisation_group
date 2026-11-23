from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

workbook = Path(
    r"C:\Users\eabha\OneDrive\Documents\a.dataVisualisation\group project"
    r"\PAQ_L_Visualisation_Ready.xlsx"
)

sheet = "Clean Data - gpt"
x_column = "Vigorous activity duration (minutes/session)"
y_column = "Sitting time (hours/day)"

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[x_column, y_column],
)

plt.boxplot(
    [data[x_column].dropna(), data[y_column].dropna()],
    tick_labels=[
        "Vigorous activity\n(minutes/session)",
        "Sitting time\n(hours/day)",
    ],
)
plt.ylabel("Values (the two datasets use different units)")
plt.title("Vigorous activity duration and daily sitting time")
plt.tight_layout()
plt.show()
