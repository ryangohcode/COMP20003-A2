import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.series import Series

PATH_FILE= "../stitched_datasets/vax-active-by-lga.csv"

df = pd.read_csv(PATH_FILE)
lga_column = df["LGA"]
df=df[['% Dose 2']]
df = df.set_index(lga_column)
df = df.sort_values('% Dose 2')
print(df.to_string())
plt.figure(figsize=(10,10))
plt.boxplot(df, showmeans=True)
plt.xlabel("Victoria")
plt.xticks([1],[" "])
plt.ylabel("Percentage of people vaccinated against COVID-19")
plt.suptitle('Percentage of people vaccinated against COVID-19 in Victoria boxplot', fontsize=20, fontweight='bold')
plt.savefig('../visualisation_graphs/boxplot-vaccinated.png')
plt.show()
plt.close()