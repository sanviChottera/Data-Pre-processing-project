#merge dwarf_stars.csv and unit_converted_stars.csv
import csv
import pandas as pd

dataset1 = []
dataset2= []

with open("bright_stars.csv","r") as f:
    c = csv.reader(f)
    for i in c:
        dataset1.append(i)


with open("unit_converted_stars.csv","r") as f:
    c = csv.reader(f)
    for i in c:
        dataset2.append(i)


header1 = dataset1[0]
planet_data1 = dataset1[1:]


header2 = dataset2[0]
planet_data2 = dataset2[1:]


headers = header1 + header2
star_data = []
for i in planet_data1:
    star_data.append(i)

for i in planet_data2:
    star_data.append(i)


with open("total_stars.csv","w") as f:
    c = csv.writer(f)
    c.writerow(headers)
    c.writerows(star_data)

df = pd.read_csv("total_stars.csv")
df.tail(8)