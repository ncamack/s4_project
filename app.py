import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels
import numpy as np

# Load CSVs into DataFrames
constructors = pd.read_csv('f1_1950_2022_constructors.csv', encoding='Windows-1252')
drivers = pd.read_csv('f1_1950_2022_drivers.csv', encoding='Windows-1252')
race_results = pd.read_csv('f1_1950_2022_race_results.csv', encoding='Windows-1252')

# page configuration
st.set_page_config(layout='wide')

# title and info
st.header('Assorted Formula 1 Historical Statistics')

### GRAND PRIX TOTALS BY YEAR 

# define Grand Prix Totals by Year chart function
def grand_prix_total_by_year():

    # description
    st.write('''This bar chart shows the total amount of times each Grand Prix has been run, based on the selected year. Use slider to select which year you would like to see data through.''')
    
    # create three-column layout to limit slider size
    col1, col2, col3 = st.columns([1, 2, 1])

    # create year slider in middle column
    min_year = int(race_results['season'].min())
    max_year = int(race_results['season'].max())
    year = col2.slider('Select Year:', min_value=min_year, max_value=max_year)

    # year filter
    year_filter = race_results[race_results['season'] <= year]

    # Remove duplicate rows
    year_filter = year_filter.drop_duplicates(subset=['season', 'race_name'])

    # count number of unique races for each year
    race_counts = year_filter.groupby('race_name')['season'].nunique().reset_index(name='count')

    # create bar chart and modify appearance
    grand_prix_by_year = px.bar(race_counts, 
                                x='race_name', 
                                y='count', 
                                labels={'race_name': '• Grand Prix •', 'count': '• Total Times Run •'},
                                color='count', # colors bars based on count
                                color_continuous_scale=['#FC8585', '#FBDBA2', '#85CBD9'],  # set custom color scale
                                range_color=[0, race_counts['count'].max()],  # set custom color scale range
    )
    grand_prix_by_year.update_xaxes(tickmode='linear', tick0=0, dtick=1) # fix x axis scaling issues
    grand_prix_by_year.update_yaxes(tickvals=np.arange(race_counts['count'].min(), race_counts['count'].max()+1, step=2)) # fix y axis scaling issues
    grand_prix_by_year.update_layout(height=700,
                                     width=1000,
                                     title={'text': "Grand Prix Total by Year",
                                            'y': 0.95,
                                            'x': 0.5,
                                            'xanchor': 'center',
                                            'yanchor': 'top'
                                           }
    )

    # add rectangle shape around chart area
    grand_prix_by_year.add_shape(type="rect",
                                 xref="paper",
                                 yref="paper",
                                 x0=0,
                                 y0=0,
                                 x1=1,
                                 y1=1,
                                 fillcolor='white',
                                 opacity=0.1
    )

    # plot bar chart
    st.plotly_chart(grand_prix_by_year, use_container_width=True)

### DRIVER RACE RESULTS

# define winners by country chart function
def driver_race_results():

    # description
    st.write('''This bar chart shows the chosen drivers total race results over their entire career. You can type directly into the dropdown to search for a specific driver.''')

    # driver selectbox
    select_driver = st.selectbox('Select a driver:', sorted(race_results['driver'].unique()))

    # filter data
    driver_filter = race_results[(race_results['driver'] == select_driver) & (race_results['position'] <= 20)]

    # tally finishing positions
    position_counts = driver_filter['position'].value_counts()

    # create chart and modify
    driver_race_results = px.bar(position_counts, 
                                 x=position_counts.index, 
                                 y='position', 
                                 labels={'index': '• Finishing Position •', 'position': '• Total •'},
                                 color='position',
                                 color_continuous_scale=['#FFFF67', '#FF846A', '#C43D53', '#6B2B74', '#90CC66']
    )
    driver_race_results.update_xaxes(tickmode='linear', tick0=0, dtick=1) # fix x axis scaling issues

    # fix title
    driver_race_results.update_layout(height=700,
                                      width=1000,
                                      title={'text': "Driver Race Results",
                                             'y': 0.95,
                                             'x': 0.5,
                                             'xanchor': 'center',
                                             'yanchor': 'top'
                                            }
    )

    # add rectangle shape around chart area
    driver_race_results.add_shape(type="rect",
                                  xref="paper",
                                  yref="paper",
                                  x0=0,
                                  y0=0,
                                  x1=1,
                                  y1=1,
                                  fillcolor='white',
                                  opacity=0.1
    )
 
    # plot
    st.plotly_chart(driver_race_results, use_container_width=True)

### DRIVER QUALIFYING RESULTS

# define winners by country chart function
def driver_quali_results():

    # description
    st.write('''This bar chart shows the chosen drivers total qualifying results over their entire career. You can type directly into the dropdown to search for a specific driver.''')

    # driver selectbox
    select_driver = st.selectbox('Select a driver:', sorted(race_results['driver'].unique()))

    # filter data
    driver_filter = race_results[(race_results['driver'] == select_driver) & (race_results['grid'] <= 20)]

    # tally finishing positions
    position_counts = driver_filter['grid'].value_counts()

    # create chart and modify
    driver_quali_results = px.bar(position_counts, 
                                  x=position_counts.index, 
                                  y='grid', 
                                  labels={'index': '• Qualifying Position •', 'grid': '• Total •'},
                                  color='grid',
                                  color_continuous_scale=['#FFFF67', '#FF846A', '#C43D53', '#6B2B74', '#90CC66']
                                 )

    # fix x axis scaling issues
    driver_quali_results.update_xaxes(tickmode='linear', tick0=0, dtick=1) 

    # fix title
    driver_quali_results.update_layout(height=700,
                                       width=1000,
                                       title={'text': "Driver Quali Results",
                                              'y': 0.95,
                                              'x': 0.5,
                                              'xanchor': 'center',
                                              'yanchor': 'top'
                                             }
    )

    # add rectangle shape around chart area
    driver_quali_results.add_shape(type="rect",
                                   xref="paper",
                                   yref="paper",
                                   x0=0,
                                   y0=0,
                                   x1=1,
                                   y1=1,
                                   fillcolor='white',
                                   opacity=0.1
    )
 
    # plot
    st.plotly_chart(driver_quali_results, use_container_width=True)

### DRIVER NATIONALITY

#define driver nationality function
def driver_nationality():

    # description
    st.write('''This pie chart shows the breakdown of all drivers, based on their nationalities.''')

    # create new full name column
    drivers['full_name'] = drivers['first_name'] + ' ' + drivers['last_name']

    # filter driver nationality
    driver_nationality_count = drivers['nationality'].value_counts()

    # create pie chart
    driver_nationality = px.pie(driver_nationality_count, 
                                values='nationality', 
                                names=driver_nationality_count.index,
                                labels={'index': 'Nationality', 'nationality': 'Total Drivers'}, 
    )
    
    # update layout
    driver_nationality.update_layout(margin=dict(t=100, b=100))

    # fix title
    driver_nationality.update_layout(height=700,
                                     width=1000,
                                     title={'text': "Driver Nationality",
                                            'y': 0.95,
                                            'x': 0.455,
                                            'xanchor': 'center',
                                            'yanchor': 'top'
                                           }
    )

    # plot
    st.plotly_chart(driver_nationality, use_container_width=True)

### CONSTRUCTOR NATIONALIITY

# define constructor nationality function
def constructor_nationality():

    # description
    st.write('''This pie chart shows the breakdown of all constructers, based on their nationalities.''')

    # filter constructor nationality
    constructors_unique = constructors.drop_duplicates(subset=['name', 'nationality'])
    constructor_nationality_count = constructors_unique['nationality'].value_counts()

    # create pie chart
    constructor_nationality = px.pie(constructor_nationality_count,
                                     values='nationality',
                                     names=constructor_nationality_count.index,
                                     labels={'index': 'Nationality', 'nationality': 'Total Constructors'},
    )

    # update layout
    constructor_nationality.update_layout(margin=dict(t=100, b=190))

    # fix title
    constructor_nationality.update_layout(height=700,
                                          width=1000,
                                          title={'text': "Constructor Nationality",
                                                 'y': 0.95,
                                                 'x': 0.455,
                                                 'xanchor': 'center',
                                                 'yanchor': 'top'
                                                },
                                         )

    # plot
    st.plotly_chart(constructor_nationality, use_container_width=True)

### START VS FINISH

# define start vs finish function
def start_to_finish():

    # description
    st.write('''This scatterplot shows the comparison of starting position to finishing position for whichever drivers you wish. Modify the list on the right side using the dropdown to select specific drivers 
             or you can check "Select All" to see all drivers at once. You can type in the dropdown to search for a specific driver.''')

    # create two columns
    col1, col2, col3 = st.columns([6, 1, 3])

    # get list of unique drivers
    drivers = race_results['driver'].unique()

    # create list of default drivers
    default_drivers = ['Valtteri Bottas', 
                       'Guanyu Zhou', 
                       'Pierre Gasly', 
                       'Yuki Tsunoda', 
                       'Fernando Alonso', 
                       'Esteban Ocon', 
                       'Lance Stroll', 
                       'Charles Leclerc', 
                       'Carlos Sainz', 
                       'Daniel Ricciardo', 
                       'Kevin Magnussen',
                       'Nico Hülkenberg',
                       'Lando Norris',
                       'Lewis Hamilton',
                       'George Russell',
                       'Max Verstappen',
                       'Alexander Albon',
                      ]

    # create 'Select All' checkbox
    if col3.checkbox('Select All', value=False):
        selected_drivers = drivers
    else:
        selected_drivers = []

    # create multiselect dropdown
    selected_drivers = col3.multiselect('Select Drivers', drivers, default=default_drivers)

    # filter data by selected drivers
    if selected_drivers:
        filtered_race_results = race_results[race_results['driver'].isin(selected_drivers)]
    else:
        filtered_race_results = race_results

    # filters
    avg_positions = filtered_race_results[(filtered_race_results['grid'] <= 20) & (filtered_race_results['position'] <= 20)]

    # group by driver and calculate average 'grid' and 'position'
    avg_positions = filtered_race_results.groupby('driver')[['grid', 'position']].mean().reset_index()

    # create chart
    start_to_finish = px.scatter(avg_positions, 
                                 x='grid', 
                                 y='position', 
                                 color='driver',
                                 labels={'grid': 'Finishing Position', 'position': 'Starting Position'}, # change labels
                                )
    

    # plot
    col1.plotly_chart(start_to_finish, use_container_width=True)

### DRIVER NATIONALITY VS CONSTRUCTOR NATIONALITY

# define constructor vs driver function
def constructor_vs_driver_nationality():

    # description
    st.write('This heatmap shows how often the nationality of a driver matches the nationality of the constructor they are driving for.')

    # combine first and last names
    drivers['full_name'] = drivers['first_name'] + ' ' + drivers['last_name']

    # merge df
    cvdn_merge = pd.merge(race_results, drivers, left_on='driver', right_on='full_name')

    # keep only the unique pairs of drivers and constructors
    unique_pairs = cvdn_merge[['full_name', 'constructor', 'nationality']].drop_duplicates()

    # merge unique pairs with the constructors df to get constructor nationality
    result = pd.merge(unique_pairs, constructors, left_on='constructor', right_on='name')

    # rename the nationality_x and nationality_y columns
    result = result.rename(columns={'nationality_x': 'nationality_driver', 'nationality_y': 'nationality_constructor'})

    # drop duplicates from the result DataFrame
    result = result.drop_duplicates(subset=['full_name', 'constructor'])

    # create a crosstab of the driver and constructor nationalities
    cvdn_crosstab = pd.crosstab(result['nationality_driver'], result['nationality_constructor'])

    # create heatmap
    constructor_vs_driver_nationality = px.imshow(cvdn_crosstab, 
                                                  color_continuous_scale=['#ff2f00', '#00ffbb', '#5e00ff', '#ffae00']
                                                 )

    # update layout
    constructor_vs_driver_nationality.update_layout(height=900,
                                                    width=2000, 
                                                    title=dict(text='Driver vs Constructors Nationality',
                                                               x=0.4
                                                              ),
                                                    xaxis=dict(title='Constructor Nationality',
                                                               tickangle=-45,  
                                                               tickfont=dict(size=10),
                                                               tickmode='array'
                                                              ),
                                                    yaxis=dict(title='Driver Nationality',
                                                            )
                                                   )
    
    # show heatmap
    st.plotly_chart(constructor_vs_driver_nationality, use_container_width=True)

    # fix title
    
### RACES PER SEASON

# define races per season funciton
def races_per_season():

    # group data
    races_per_season_group = race_results.groupby('season')['round'].nunique().reset_index(name='num_races')

    # create histogram
    races_per_season = px.histogram(races_per_season_group, 
                                    x='num_races', 
                                    nbins=20,
                                    color='num_races',
                                    color_discrete_sequence=px.colors.sequential.Reds,
                                    labels={'num_races': 'Total Races'},
                                    title='Distribution of Races Held Per Year'
                                   )
    
    # update y axis label
    races_per_season.update_layout(yaxis_title='Total Seasons')

    # show histogram
    st.plotly_chart(races_per_season, use_container_width=True)

### HOME INFO
    
# define home info function
def home_info():

    # write out instructions
    st.write('In the dropdown above you will find information for Formula 1 from the years 1950 - 2022')                        

### SELECT DESIRED CHART

# creates options for dropdown
chart_options = ['Home', 
                 'Average Start to Finish', 
                 'Constructor Nationality',
                 'Constructor Nationality vs Driver Nationality', 
                 'Driver Nationality', 
                 'Driver Qualifying Results', 
                 'Driver Race Results', 
                 'Grand Prix Total by Year',
                 'Races Per Season'
                 ] 

# create dropdown to select chart
selected_chart = st.selectbox('Please select and option from the dropdown below.', chart_options)

# display (call) correct chart
if selected_chart == 'Grand Prix Total by Year':
    grand_prix_total_by_year()
elif selected_chart == "Driver Race Results":
    driver_race_results()
elif selected_chart == "Driver Qualifying Results":
    driver_quali_results()
elif selected_chart == "Driver Nationality":
    driver_nationality()
elif selected_chart == 'Constructor Nationality':
    constructor_nationality()
elif selected_chart == 'Average Start to Finish':
    start_to_finish()
elif selected_chart == 'Constructor Nationality vs Driver Nationality':
    constructor_vs_driver_nationality()
elif selected_chart == 'Home':
    home_info()
elif selected_chart == 'Races Per Season':
    races_per_season()