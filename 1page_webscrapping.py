from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(".titleline")
subtext = soup.select(".subtext")



def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points >= 100:
                info = hn.append({"title": title,
                                  "url": href,
                                  "points": points})

    return hn

def sort_by_votes(hn):
    return sorted(hn, key= lambda k:k["votes"], reverse=True)


pprint.pprint(create_custom_hn(links, subtext))
