import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.series import Series

PATH_FILE= "../cleaned_datasets/active_cases_by_lga.csv"

df = pd.read_csv(PATH_FILE)
df = df.sort_values('active-cases',ascending=False).head(10)
#produce bar chart
print(df.to_string())
lga_column = df["LGA"]
active_column = df["active-cases"]
plt.bar(lga_column,active_column)
plt.xticks( lga_column,lga_column, rotation=80)
plt.subplots_adjust(wspace=0.6, hspace=2, left=0.1, bottom=0.4, right=0.96, top=0.96)
plt.xlabel("LGA names")
plt.ylabel("Number of active cases")
plt.suptitle('Bar chart of the top 10 highest number of active covid cases by LGA', fontsize=8, fontweight='bold')
#plt.savefig('../visualisation_graphs/active_cases_barchart.png')
plt.show()
plt.close()