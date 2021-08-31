# Jordan Lerma
# 2021 August 31
# Opens Airbnb reservations as new tabs in chrome
# RES ID in my csv file is the unique confirmation code for each reservation

import webbrowser
import pandas as pd

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
resList = pd.read_csv(r"c:/Users/Jordan Lerma/Documents/july.csv")
url_temp = "www.airbnb.com/hosting/reservations/details/"


#Open all the reservations in the resList in chrome tabs
for i in resList.loc[:, "RES ID"]:
  url = url_temp + i
  webbrowser.get(chrome_path).open(url)
  print(i)