import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.series import Series

PATH_FILE= "../stitched_datasets/vax-active-by-lga.csv"

df = pd.read_csv(PATH_FILE)
lga_column = df["LGA"]
df=df[['active-cases']]
df = df.set_index(lga_column)
df = df.sort_values('active-cases')
print(df.to_string())
plt.figure(figsize=(10,10))
plt.boxplot(df, showmeans=True)
plt.xlabel("Victoria")
plt.xticks([1],[" "])
plt.ylabel("Number of active COVID-19 cases")
plt.suptitle('Number of active COVID-19 cases in Victoria box plot', fontsize=20, fontweight='bold')
plt.savefig('../visualisation_graphs/boxplot-active-cases.png')
plt.show()
plt.close()