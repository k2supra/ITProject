

import csv
import re
try:
   while True:

      datafile = "data.csv"
      csv_columns = ["login", "password"]
      data = [
         {"login": "yaroslav", "password": "1111"},
         {"login": "andrey", "password": "2222"},
         {"login": "oleg", "password": "3333"}
      ]
      with open(datafile, "w") as csvfile:
         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
         writer.writeheader()
         writer.writerows(data)
      print("==========Log in==========")  # 24
      loginwh = input("Login: ")
      passwordwh = input("Password: ")
      with open(datafile, "r") as csvfile:
         acc1 = csvfile.readlines()
         res1 = re.split(" |\n|''|,", acc1[2])
         res2 = re.split(" |\n|''|,", acc1[4])
         res3 = re.split(" |\n|''|,", acc1[6])
         res = res1, res2, res3

      for line in res:
         if loginwh == line[0] and passwordwh == line[1]:
            print("\033[1;32;40m Log in was successful!\033[0m")
            break
      else:
         print("\033[1;31;40m Invalid login or password\033[0m")
         continue
      break
except Exception as e:
   print(e)

name = input("Enter the name of your file: ")
directory = str(input("Enter the path where you want to save your file: "))

csv_columns = ['No','Product','Category','Amount','About','Price','Shop/s']
dict_data1 = [
{'No': 1, 'Product': 'Car', 'Category': 'Transport', 'Amount': '3', 'About': 'Fast indian car', 'Price': '1000$'},
{'No': 2, 'Product': 'Cooler', 'Category': 'House thing', 'Amount': '1', 'About': 'Plastic chinese thing', 'Price': '150$'},
{'No': 3, 'Product': 'Refrigerator', 'Category': 'House thing', 'Amount': '2', 'About': 'Refrigerator', 'Price': '6000$'},
{'No': 4, 'Product': 'Mouse PC.', 'Category': 'PC accessory', 'Amount': '2', 'About': 'PC`s', 'Price': '700$'},
{'No': 5, 'Product': 'Stickers', 'Category': 'For kids', 'Amount': '1', 'About': 'Stickers "Hello Kitty"', 'Price': '9700$'},
{'No': 6, 'Product': 'TV', 'Category': 'Multimedia', 'Amount': '5', 'About': 'Colored TV', 'Price': '9300$'},
]

csv_file = (directory + "\\" + name + ".csv")
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