
# with open("weather_data.csv") as data_files:
#     data = data_files.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
#
# # Getting data in columns
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# Getting data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
# print(monday.condition)
temp = monday.temp
print((temp * 9/5) + 32)


