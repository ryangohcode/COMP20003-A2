import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.series import Series

PATH_FILE= "../stitched_datasets/vax-active-by-lga.csv"

df = pd.read_csv(PATH_FILE)
df = df.sort_values('% Dose 2',ascending=False).head(10)
#produce bar chart
print(df.to_string())
lga_column = df["LGA"]
vaccinated_column = df["% Dose 2"]
plt.bar(lga_column,vaccinated_column)
plt.xticks( lga_column,lga_column, rotation=80)
plt.subplots_adjust(wspace=0.6, hspace=2, left=0.1, bottom=0.4, right=0.96, top=0.96)
plt.xlabel("LGA names")
plt.ylabel("Percentage of people vaccinated against COVID-19 (%)")
plt.suptitle('Bar chart of the top 10 highest percentage of people vaccinated against COVID-19 by LGA in Victoria', fontsize=8, fontweight='bold')
plt.savefig('../visualisation_graphs/vaccinated_barchart.png')
plt.show()
plt.close()