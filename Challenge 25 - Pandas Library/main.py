import pandas as pd
import csv

# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1].isnumeric():
#             temperature.append(int(row[1]))
#
#     print(temperature)

# df = pd.read_csv('./weather_data.csv')
#
# monday = df[df.day == 'Monday']
# temp_in_f = (monday.temp * (9/5)) + 32
# print(monday.temp)
# print(temp_in_f)

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grouped_df = df.groupby('Primary Fur Color')['Primary Fur Color'].count().sort_values(ascending=False)
grouped_df.to_csv('squirrel_count.csv')
