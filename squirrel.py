import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250303.csv")

black = len(squirrel[squirrel["Primary Fur Color"] == "Black"])
cinnamon = len(squirrel[squirrel["Primary Fur Color"] == "Cinnamon"])
gray = len(squirrel[squirrel["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Black", "cinnamon", "Gray"],
    "Count": [black, cinnamon, gray]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrels.csv")
