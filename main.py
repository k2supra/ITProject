import csv
name = input("Enter the name of your file") ####2222####
directory = str(input("Enter the path where you want to save your file->"))

csv_columns = ['No','Product','Category','Amount','About','Price','Shop/s'] ########3333333333##########
dict_data1 = [
{'No': 1, 'Product': 'Car', 'Category': 'Transport', 'Amount': '3', 'About': 'Fast indian car', 'Price': '1000$'},
{'No': 2, 'Product': 'Cooler', 'Category': 'House thing', 'Amount': '1', 'About': 'Plastic chinese thing', 'Price': '150$'},
{'No': 3, 'Product': 'Refrigerator', 'Category': 'House thing', 'Amount': '2', 'About': 'Refrigerator', 'Price': '6000$'},
{'No': 4, 'Product': 'Mouse PC.', 'Category': 'PC accessory', 'Amount': '2', 'About': 'PC`s', 'Price': '700$'},
{'No': 5, 'Product': 'Stickers', 'Category': 'For kids', 'Amount': '1', 'About': 'Stickers "Hello Kitty"', 'Price': '9700$'},
{'No': 6, 'Product': 'TV', 'Category': 'Multimedia', 'Amount': '5', 'About': 'Colored TV', 'Price': '9300$'},
]
csv_file = (directory + "\\" + name + ".csv") ####2222####
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data1:
            writer.writerow(data)

    with open(csv_file, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            for index in range(0, len(row)):
                print(row[index], end='\t')
            print()


except IOError as ex:
    print(f"I/O error::{ex}")

