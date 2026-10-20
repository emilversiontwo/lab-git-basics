# считаем сколько всего расчетов во всех пожарных частях
import csv

total = 0
max_crews = 0
with open("stations.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        crews = int(row["crews"])
        total = total + crews
        # заодно ищем самую большую часть
        if crews > max_crews:
            max_crews = crews

print("Всего расчетов:", total)
print("Больше всего расчетов в одной части:", max_crews)
