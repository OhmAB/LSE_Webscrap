from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.lse.ac.uk/study-at-lse/undergraduate/degree-programmes-2024/ba-history")
soup = BeautifulSoup(response.text, 'html.parser')

column_index_1 = 1 
column_index_0 = 0
c =[]
data_0 = []
data_1 = []


#Brief Description :
description = soup.findes = soup.find("div", class_="courseSummary").find("p").text.strip()
data_0.append("Description")
data_1.append(description)


#Degree :
degree = soup.find("li" , class_="keyDetails__item--grad").text
data_0.append("Degree")
data_1.append(degree)


# Application and Duration :
table = soup.find('table')

for row in table.find_all('tr'):
    columns = row.find_all(['th', 'td'])
    if columns: 
        data_0.append(columns[column_index_0].get_text(strip=True))
        data_1.append(columns[column_index_1].get_text(strip=True))
        

#Eligibility : 
accord_content_data = soup.find_all("div",class_= "accordion__content")


eligible = accord_content_data[1].find_all("p")

for i in range(len(eligible)):
    c.append(eligible[i].get_text(strip=True))
concatenated_string = ' '.join(c)
data_0.append("Eligibility")
data_1.append(concatenated_string)

#Overseas Student Fee :
Overseas_fee = accord_content_data[3].find_all("p")[4].text.strip()
data_0.append("Overseas Student")
data_1.append(Overseas_fee)


df = pd.DataFrame({'column1': data_0, 'column2': data_1})
left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
display(left_aligned_df)


