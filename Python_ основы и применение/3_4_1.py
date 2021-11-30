import csv
with open('Crimes.csv') as file_csv:
    reader_file = csv.DictReader(file_csv)
    list_primary_type =[]
    for row in reader_file:
        date_row = int(row['Date'][6:11])
        if int(date_row) == 2015 :
            list_primary_type.append(row['Primary Type'])
    print(max(list_primary_type, key=lambda x:list_primary_type.count(x)))