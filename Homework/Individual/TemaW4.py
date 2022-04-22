from bs4 import BeautifulSoup
import requests as req
import pandas as pd

r = req.get("https://frsah.ro/")
link = BeautifulSoup(r.text, "html.parser")

title = link.find_all('table', attrs={'class' : 'wptb-preview-table wptb-element-main-table_setting-18262'})
# print(link)
# print(title)

td_list = []
dataset = []
header = []
saveHeaderFlag = True
for i in title:
    for tr_index in i.find_all('tr'):
        # print("row")
        # print(tr_index)
        td_list = []
        for td_index in tr_index.find_all('td'):
            for div_text_containers in td_index.find_all('div'):
                for values in div_text_containers.find_all('div'):
                    td_list.append(values.get_text()) # find all table data for a row ( 2 divs in the td_index)
        # print("exit_row")
        if saveHeaderFlag: # flag used to save the headers ( make it false after retrieving the first row)
            header = td_list
            saveHeaderFlag = False
        else:
            dataset.append(td_list) # append it to the dataset if not the headers of the dataset

df = pd.DataFrame(dataset, columns = header)
df.to_csv("ChessChampionships.csv", header = header)


