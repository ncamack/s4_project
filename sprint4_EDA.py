# imports
import pandas as pd
import csv

# Read CSVs
constructors = pd.read_csv('f1_1950_2022_constructors.csv', encoding='Windows-1252')
drivers = pd.read_csv('f1_1950_2022_drivers.csv', encoding='Windows-1252')
race_results = pd.read_csv('f1_1950_2022_race_results.csv', encoding='Windows-1252')

# remove blank rows and save
def remove_blank_rows(file_name):
    with open(file_name, mode='r') as f:
        reader = csv.reader(f)
        data = [row for row in reader if any(field.strip() for field in row)]
    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

remove_blank_rows('f1_1950_2022_race_results.csv')
remove_blank_rows('f1_1950_2022_drivers.csv')
remove_blank_rows('f1_1950_2022_constructors.csv')

# split drivers name into first and last in 'race_results' and add columns to match 'drivers' and save
names = race_results['driver'].str.split(' ', expand=True)
race_results['first_name'] = names[0]
race_results['last_name'] = names[1]
race_results.to_csv('f1_1950_2022_race_results.csv', index=False)

# Make lowercase to ensure consistency
constructors['name'] = constructors['name'].str.lower()
constructors['nationality'] = constructors['nationality'].str.lower()
drivers['nationality'] = drivers['nationality'].str.lower()
drivers['first_name'] = drivers['first_name'].str.lower()
drivers['last_name'] = drivers['last_name'].str.lower()
race_results['race_name'] = race_results['race_name'].str.lower()
race_results['first_name'] = race_results['first_name'].str.lower()
race_results['last_name'] = race_results['last_name'].str.lower()
race_results['constructor'] = race_results['constructor'].str.lower()
