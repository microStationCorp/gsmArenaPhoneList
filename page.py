from bs4 import BeautifulSoup
import requests
import json


class testSujan:
    def getPhoneList(self, urlGet, linkDict, flag=None):
        re = requests.get(urlGet)
        soup = BeautifulSoup(re.content, "html.parser")
        li = soup.find('div', class_='makers').find_all('li')
        for i in li:
            siteLink = "https://www.gsmarena.com/" + i.a.get("href")
            imgLink = i.a.img.get("src")
            name = i.a.strong.span.text
            linkDict.update({
                name: {
                    "url": siteLink,
                    "image": imgLink
                }
            })
        if flag == None:
            navs = soup.find_all('div', class_="nav-pages")
            if len(navs) != 0:
                for nav in navs:
                    anchor = nav.find_all('a')
                    for a in anchor:
                        newUrl = "https://www.gsmarena.com/" + a.get("href")
                        self.getPhoneList(newUrl, linkDict, True)
        return linkDict


if __name__ == '__main__':
    url = "https://www.gsmarena.com/acer-phones-59.php"
    linkDict = dict()
    linkDict = testSujan().getPhoneList(url, linkDict)
    print(json.dumps(linkDict, indent=4))
