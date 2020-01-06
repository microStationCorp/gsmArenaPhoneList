from bs4 import BeautifulSoup
import requests
import json
import page

mainDict = dict()

url = "https://www.gsmarena.com/makers.php3"
re = requests.get(url)
soup = BeautifulSoup(re.content, "html.parser")
table = soup.find_all('table')
anchor = table[0].find_all('a')

for a in anchor:
    name = a.text[:-8]
    while name[len(name) - 1].isdigit():
        name = name[:-1]
    link = "https://www.gsmarena.com/" + a.get("href")
    mainDict.update({
        name: {
            "link": link,
            "mobile": {}
        }
    })

for key in mainDict:
    print(key)
    mainDict[key]['mobile'] = page.testSujan().getPhoneList(mainDict[key]['link'], mainDict[key]['mobile'])

with open("/root/Downloads/main.json", "w") as file:
    json.dump(mainDict, file, indent=4)
