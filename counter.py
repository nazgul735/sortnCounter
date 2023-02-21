import os
import csv
import re
def counter():
    filename="peBuyBuild.csv"
    dict2018, dict2019, dict2020, dict2021, dict2022, dict2023={}, {}, {}, {}, {}, {}
    companySet=set()
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
                i = re.sub('"', '', i)
                if i[0]==" ":
                    i=i[1:]
                companySet.add(i)
                if first=="2018":
                    dict2018[i]=dict2018[i]+1 if i in dict2018 else 1
                elif first=="2019":
                    dict2019[i]=dict2019[i]+1 if i in dict2019 else 1
                elif first=="2020":
                    dict2020[i]=dict2020[i]+1 if i in dict2020 else 1
                elif first=="2021":
                    dict2021[i]=dict2021[i]+1 if i in dict2021 else 1
                elif first=="2022":
                    dict2022[i]=dict2022[i]+1 if i in dict2022 else 1
                elif first=="2023":
                    dict2023[i]=dict2023[i]+1 if i in dict2023 else 1
    csvfile.close()
    with open("output.csv", 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["PE Fund", 2018, 2019, 2020, 2021, 2022, 2023])
        for j in companySet:
            temp2018, temp2019, temp2020, temp2021, temp2022, temp2023=0,0,0,0,0,0
            if j in dict2018:
                temp2018=dict2018[j]
            elif j in dict2019:
                temp2019=dict2019[j]
            elif j in dict2020:
                temp2020=dict2020[j]    
            elif j in dict2021:
                temp2021=dict2021[j]
            elif j in dict2022:
                temp2022=dict2022[j]
            elif j in dict2023:
                temp2023=dict2023[j]
            writer.writerow([j, temp2018, temp2019, temp2020, temp2021, temp2022, temp2023])
counter()
