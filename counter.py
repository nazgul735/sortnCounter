import os
import csv
def counter():
    filename="peTransactions.csv"
    dict2018, dict2019, dict2020, dict2021, dict2022, dict2023={}, {}, {}, {}, {}, {}
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        temp=True
        for row in spamreader:
            if temp==True:
                temp=False
                continue
            first=row[0][6:]
            # print(row[1:][0])
            for i in row[1:]:
                
                
                if first=="2018":
                    return
                elif first=="2019":
                    return
                elif first=="2020":
                    return
                elif first=="2021":
                    return
                elif first=="2022":
                    return
                elif first=="2023":
                    return
           

counter()