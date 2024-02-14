import csv
with open("space.txt", encoding="utf-8") as file:
    data = list(csv.DictReader(file, delimiter = "*"))
print(data)
for i in data:
    if i['coord_place'] == '0 0':
        name_ship = i['ShipName'].split("-")
        n = int(name_ship[1][0])
        m = int(name_ship[1][1])
        t = len(i['planet'])
        direction = i['direction'].split()
        xd = int(direction[0])
        yd = int(direction[1])
        if n > 5:
            x = n + xd
        else:
            x = -(n + xd) * 4 + t
        if m > 3:
            y = m + t + yd
        else:
            y = -(n + yd) * m
        i['coord_place'] = str(x) + " " + str(y)
with open("space_new.txt", "w", newline = "", encoding="utf-8") as file1:
    w = csv.writer(file1)
    w.writerow(data)

