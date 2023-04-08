#!/bin/python3

# Create a squirrel data set that stores fur, color, and ege of squirrels

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Access relevant data
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Build a dict to later build a data frame
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

data_df = pandas.DataFrame(data_dict)

# Convert data frame to csv
data_df.to_csv("squirrel_count.csv")