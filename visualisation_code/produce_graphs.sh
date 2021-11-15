#!/bin/bash
echo "Producing Active Cases heatmap"
python3 heatmap-active-cases.py
echo "Producing Vaccination Rates 1 heatmap"
python3 heatmap-vax-rates-1.py
echo "Producing Vaccination Rates 2 heatmap"
python3 heatmap-vax-rates-2.py
echo "Merged heatmap"
python3 heatmap-active-vax-1.py
echo "Merged heatmap 2"
python3 heatmap-active-vax-2.py
