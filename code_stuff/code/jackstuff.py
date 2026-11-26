from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

workbook = (
    Path(file).resolve().parents[2]
    / "Excel Files"
    / "PAQ_L_Visualisation_Ready.xlsx"
)

#Visualisation 1
sheet = "Transformed Data - Sean"
dataS = "Sedentary Hours per year"
y_column0 = "# of people"
y_column1 = []
x_column1 = []

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[dataS],
).dropna(subset=[dataS])

values = data[dataS].dropna()
loopcount = 29
for i in range(1, loopcount):
    lower = (i - 1) * 240
    upper = i * 240
    y_column1.append((values.gt(lower) & values.le(upper)).sum())
    x_column1.append(f"{lower} - {upper}")

plt.barh(y_column1, x_column1)
plt.ylabel("# of people")
plt.xlabel("Time spent per 240 hours")
plt.title("Number of people per sitting time")
plt.tight_layout()
plt.show()

#Visualisation 2
sheet = "Aggregted Data - Sean"
label_column = "Vigorous Activity Timespan"
count_column = "Vigorous Activity Timespan Count"

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[label_column, count_column],
).dropna(subset=[label_column, count_column])

plt.barh(data[label_column], data[count_column])
plt.ylabel("# of people")
plt.xlabel("Time spent per 36 hours")
plt.title("Number of people per vigorous activity time")
plt.tight_layout()
plt.show()

#Visualisation 3
sheet = "Aggregted Data - Sean"
label_column = "Moderate Activity Timespan"
count_column = "Moderate Activity Timespan Count"

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[label_column, count_column],
).dropna(subset=[label_column, count_column])

plt.barh(data[label_column], data[count_column])
plt.ylabel("# of people")
plt.xlabel("Time spent per 36 hours")
plt.title("Number of people per moderate activity time")
plt.tight_layout()
plt.show()