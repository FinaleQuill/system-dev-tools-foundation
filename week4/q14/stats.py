import csv

with open("data.csv") as f:
    total = sum(int(row["value"]) for row in csv.DictReader(f))

open("stats.txt", "w").write(str(total))
