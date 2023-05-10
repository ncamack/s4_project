import csv

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