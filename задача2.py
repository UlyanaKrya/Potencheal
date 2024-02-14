from random import choice
def qsort(data):
    for i in range(1,len(data)):
        j = i
        x = data[i]
        while j > 0 and int(data[j]['ShipName'].split("-")[1]) > int(data[i]['ShipName'].split("-")[1]):
            data[j] = data[j - 1]
            j -= 1
        data[j] = x
    return data
import csv
with open("space.txt", encoding="utf-8") as file:
    a = list(csv.DictReader(file, delimiter = "*"))
print(qsort(a[:20]))