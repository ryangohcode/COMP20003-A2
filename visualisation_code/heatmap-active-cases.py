import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

from analyse_shapefile_lga import find_most_similar

PLOT_COLUMN = "active_cases_per_capita_norm"

def logmap(x):
    if(x == 0):
        return 0
    else:
        return np.log(x * 100)

sns.set(style="darkgrid")
#dataset = pd.read_csv("../stitching_code/vax-active-by-lga.csv")
regions = gpd.read_file("../source_data/vic_polygon_lga_shp/vic_lga.shp")
regions.plot(figsize=(40,20))
regions.rename(columns={'ABB_NAME':'LGA'}, inplace=True)
stitch_cases = pd.read_csv("../stitched_datasets/vax-active-by-lga.csv")
#plt.show()
#active_cases = pd.read_csv("../cleaned_datasets/active_cases_by_lga.csv")
#vax_rates["% Dose 2"]=vax_rates["% Dose 2"]*100;
#vax_rates['count'] = 1
#active_cases = active_cases[['LGA', 'active-cases']]
# Distinct Region LGAs for the sake of processing

region_lgas = list(set(regions['LGA'].to_list()))
# Map Vaccine Rate LGAs to the region LGAs
stitch_cases['LGA'] = stitch_cases['LGA'].map(lambda x : find_most_similar(x, region_lgas)[0])
stitch_cases[PLOT_COLUMN] = stitch_cases[PLOT_COLUMN].map(logmap)

merged = pd.merge(regions, stitch_cases, on=['LGA'], how='inner')
merged = merged.reset_index()
merged = merged.fillna(0)
merged.drop(['index','geometry'], axis=1).to_csv('merge_data.csv', index=False)

fig, ax = plt.subplots(1, figsize=(40, 20))
ax.axis('off')
ax.set_title('Victoria Active Cases Per Capita (Normalised by x=log(100x) scale)', fontdict={'fontsize': '40', 'fontweight': '3'})

color = 'hot'
vmin, vmax = 0, stitch_cases[PLOT_COLUMN].max()
sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=vmin, vmax=vmax))
cbar = fig.colorbar(sm)
cbar.ax.tick_params(labelsize=20)

#plot_victoria('% Dose 2', 'Oranges', ax)
merged.plot(PLOT_COLUMN, cmap=color, ax=ax, linewidth=0.8, edgecolor='0.8', figsize=(40, 20))

os.chdir("../visualisation_graphs")
plt.savefig('heatmap-active-cases.png', format='png')
