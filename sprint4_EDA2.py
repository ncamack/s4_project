# imports
import pandas as pd
import csv

# Read CSVs
constructors = pd.read_csv('f1_1950_2022_constructors.csv', encoding='UTF-8')
drivers = pd.read_csv('f1_1950_2022_drivers.csv', encoding='UTF-8')
race_results = pd.read_csv('f1_1950_2022_race_results.csv', encoding='UTF-8')

# Check for empty data
constructors.isnull()
drivers.isnull()
race_results.isnull()

