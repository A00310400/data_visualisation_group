from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

workbook = Path(
    r"C:\Users\seana\Downloads"
    r"\PAQ_L_Visualisation_Ready.xlsx"
)

# Visualisation 1
sheet = "Transformed Data - Sean"
x_column = "Moderate Hours per year"
y_column = "Sedentary Hours per year"

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[x_column, y_column],
).dropna(subset=[x_column, y_column])

plt.scatter(data[x_column], data[y_column], alpha=1)
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title("Yearly moderate activity vs sitting time")
plt.tight_layout()
plt.show()

# Visualisation 4
sheet = "Aggregted Data - Sean"
labels = "Moderate Activity Timespan"
sizes = "Moderate Activity Timespan Count"

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[labels, sizes],
).dropna(subset=[labels, sizes])

fig, ax = plt.subplots()

plt.pie(data[sizes], labels=data[labels], autopct='%1.1f%%')
plt.title("Participants by Moderate activity hours per year")
plt.tight_layout()
plt.show()

# Visualisation 5
sheet = "Aggregted Data - Sean"
labels = "Vigorous Activity Timespan"
sizes = "Vigorous Activity Timespan Count"

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[labels, sizes],
).dropna(subset=[labels, sizes])

fig, ax = plt.subplots()

plt.pie(data[sizes], labels=data[labels], autopct='%1.1f%%')
plt.title("Participants by Vigorous activity hours per year")
plt.tight_layout()
plt.show()