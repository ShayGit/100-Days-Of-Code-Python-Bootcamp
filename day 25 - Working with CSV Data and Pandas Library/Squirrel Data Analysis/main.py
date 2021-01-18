# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
#
#
# data = pandas.read_csv("weather_data.csv")
#  print(type(data))
#  print(data)
#
#
# data_dict = data.to_dict()
# print(data_dict)
#
#
# monday = data[data.day == 'Monday']
#
# print(int(monday.temp) * 9 / 5 + 32)
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
             "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")