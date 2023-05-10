import requests
import csv

start_season = 1950
end_season = 2022

#retrieve race information
with open(f'f1_{start_season}_{end_season}_race_results.csv', mode='w') as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['Season', 'Round', 'RaceName', 'Driver', 'Constructor', 'Grid', 'Position'])
    # Write the data rows
    for season in range(start_season, end_season + 1):
        url = f'https://ergast.com/api/f1/{season}.json'
        response = requests.get(url)
        data = response.json()
        total_rounds = int(data['MRData']['total'])
        for round in range(1, total_rounds + 1):
            url = f'https://ergast.com/api/f1/{season}/{round}/results.json'
            response = requests.get(url)
            data = response.json()
            for race in data['MRData']['RaceTable']['Races']:
                season = race['season']
                round = race['round']
                race_name = race['raceName']
                for result in race['Results']:
                    driver = result['Driver']['givenName'] + ' ' + result['Driver']['familyName']
                    constructor = result['Constructor']['name']
                    grid = result['grid']
                    position = result['position']
                    writer.writerow([season, round, race_name, driver, constructor, grid, position])

# Retrieve driver information
with open(f'f1_{start_season}_{end_season}_drivers.csv', mode='w') as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['DriverId', 'GivenName', 'FamilyName', 'Nationality', 'DateOfBirth', 'URL'])
    # Write the data rows
    for season in range(start_season, end_season + 1):
        url = f'https://ergast.com/api/f1/{season}/drivers.json'
        response = requests.get(url)
        data = response.json()
        for driver in data['MRData']['DriverTable']['Drivers']:
            driver_id = driver['driverId']
            given_name = driver['givenName']
            family_name = driver['familyName']
            nationality = driver['nationality']
            date_of_birth = driver['dateOfBirth']
            url = driver['url']
            writer.writerow([driver_id, given_name, family_name, nationality, date_of_birth, url])

# Retrieve constructor information
with open(f'f1_{start_season}_{end_season}_constructors.csv', mode='w') as f:
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['ConstructorId', 'Name', 'Nationality', 'URL'])
    # Write the data rows
    for season in range(start_season, end_season + 1):
        url = f'https://ergast.com/api/f1/{season}/constructors.json'
        response = requests.get(url)
        data = response.json()
        for constructor in data['MRData']['ConstructorTable']['Constructors']:
            constructor_id = constructor['constructorId']
            name = constructor['name']
            nationality = constructor['nationality']
            url = constructor['url']
            writer.writerow([constructor_id, name, nationality, url])