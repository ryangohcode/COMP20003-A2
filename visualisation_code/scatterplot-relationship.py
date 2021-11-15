import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
from pandas.core.series import Series

PATH_FILE= "../stitched_datasets/vax-active-by-lga.csv"

df = pd.read_csv(PATH_FILE)
lga_column = df["LGA"]
vaccinated_column = df["% Dose 2"]
active_column = df["active-cases"]
#correlation = pd.DataFrame([df["% Dose 2"], df["active-cases"]],columns=["% Dose 2", "active-cases"])
newdf = df.filter(["active-cases","% Dose 2"], axis=1)
correlation =DataFrame.corr(newdf, method='pearson', min_periods=1)
print(correlation.to_string())
pearsoncorrelation = round(correlation.iloc[0]["% Dose 2"],3)
print(pearsoncorrelation)
for row in df.iterrows():
    plt.scatter(df["% Dose 2"], df["active-cases"],color='green',s=2)
plt.grid(True)
plt.ylim(0,3500) #changes scale
plt.yticks([50,500,1000,1500,2000,2500,3000,3500])   #ammend axis tickers
plt.ylabel("Active COVID-19 cases")
plt.xlabel("Vaccinated percentage (%)")
plt.suptitle('Scatterplot of active COVID-19 cases and vaccinated percentage in Victoria by LGA\nPearson correlation = '+str(pearsoncorrelation), fontsize=10, fontweight='bold')
plt.savefig('../visualisation_graphs/scatterplot_relationship.png')
plt.show()
plt.close()