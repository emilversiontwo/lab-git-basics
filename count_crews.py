# считаем сколько всего расчетов во всех пожарных частях
import csv

total = 0
with open("stations.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total = total + int(row["crews"])

print("Всего расчетов:", total)
