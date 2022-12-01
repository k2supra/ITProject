

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