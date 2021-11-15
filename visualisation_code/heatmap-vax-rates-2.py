import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import textdistance as td
import os
from analyse_shapefile_lga import find_most_similar

DOSAGE='% Dose 2'
sns.set(style="darkgrid")
#dataset = pd.read_csv("../stitching_code/vax-active-by-lga.csv")
regions = gpd.read_file("../source_data/vic_polygon_lga_shp/vic_lga.shp")
regions.rename(columns={'ABB_NAME':'LGA'}, inplace=True)
regions = regions.sort_values(by=['LGA'])
regions.plot(figsize=(40,20))

vax_rates = pd.read_csv("../cleaned_datasets/vaccination_rates_by_lga.csv")
# Focusing on Dose 2 for now
vax_rates = vax_rates[['LGA', DOSAGE]]
# Distinct Region LGAs for the sake of processing
region_lgas = list(set(regions['LGA'].to_list()))
# Map Vaccine Rate LGAs to the region LGAs
vax_rates['LGA'] = vax_rates['LGA'].map(lambda x : find_most_similar(x, region_lgas)[0])


# Merge Vaccine Rates and Regions on LGA. Default value: 0
merged = pd.merge(regions, vax_rates, on=['LGA'], how='inner')
merged = merged.reset_index()
merged = merged.fillna(0)

fig, ax = plt.subplots(1, figsize=(40, 20))
ax.axis('off')
ax.set_title('Dose 2 Vaccination Rates per LGA in Victoria', fontdict={'fontsize': '40', 'fontweight': '3'})

color = 'gist_rainbow'
vmin, vmax = 0, 100
sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=vmin, vmax=vmax))
cbar = fig.colorbar(sm)
cbar.ax.tick_params(labelsize=20)

merged.plot(DOSAGE, cmap=color, linewidth=0.8, ax=ax, edgecolor='0.8', figsize=(40, 20))

os.chdir("../visualisation_graphs")
plt.savefig('heatmap-vax-rates-2.png', format='png')