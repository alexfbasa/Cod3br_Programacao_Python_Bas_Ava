import csv

with open('pessoas.csv') as arquivo:
    for pessoa in csv.reader(arquivo):
        print(f"Nome {pessoa[0]}, idade {pessoa[1]}")
