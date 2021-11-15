#!/bin/bash
cd cleaning_code
echo "CLEANING ACTIVE CASES"
python3 clean-active_cases-LGA.py
echo "CLEANING VAX RATE"
python3 clean-vax-rate-LGA.py
