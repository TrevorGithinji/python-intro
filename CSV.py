import csv
from os import close

csvreader = csv.reader(open("data.csv"))
close(csvreader)
next(csvreader)
next(csvreader)

