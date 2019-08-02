import requests
import urllib.request
from bs4 import BeautifulSoup
import re

url="https://www.apple.com/itunes/charts/songs"
with urllib.request.urlopen(url) as f:
    song_list = str(f.read())

pattern="<li>(.+?)</li>"
songs=re.findall(pattern, song_list)

soup = BeautifulSoup(song_list,"html.parser")
section=soup.find('section',attrs={'class':'section chart-grid'})
results=section.find_all('li')
for result in results:
    Rank=result.find('strong').getText()
    cont=result.find_all('a')
    Song=cont[1].getText()
    Rank=Rank.replace(".","").rstrip()
    Author=cont[2].getText().strip()
    print("Rank: ",Rank,", Song: ",Song, ", Author: ", Author)

# rows.append(['Rank','Author','Song'])
#
# for result in results:
#     data=result.find('li')
#     print (data[0].getText())


