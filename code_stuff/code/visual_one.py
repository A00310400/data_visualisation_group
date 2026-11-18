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
).dropna(subset=[x_column, y_column])

plt.scatter(data[x_column], data[y_column], alpha=1)
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title("Vigorous activity duration vs daily sitting time")
plt.tight_layout()
plt.show()