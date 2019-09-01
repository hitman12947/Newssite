import requests, time
from bs4 import BeautifulSoup
from newsweb.models import NewsDb
from newsweb import db

def getNews():
    req = requests.get('https://www.bbc.com/')
    soup = BeautifulSoup(req.text, 'html.parser')

    link_text =[item.get_text().strip() for item in soup.find_all('a',class_='media__link')]
    links =[item.get('href') for item in soup.find_all('a',class_='media__link')]
    data = []
    for i in range(len(links)):
        item = (link_text[i],links[i])
        data.append(item)
    return data

def getFullNews(n_link):
    try:
        req = requests.get(f"https://www.bbc.com{n_link}")
        soup = BeautifulSoup(req.text, 'html.parser')
        heading = soup.find('h1').get_text()
        imgurl = soup.find_all('img')[1].get('src')

        if heading:
            data = {
                'status_code':req.status_code,
                'heading':heading,
                'imageurl':imgurl
            }
        else:
            data = {
                'status_code':req.status_code,
                'heading':"No heading",
                "imageurl":"No imageurl"
            }
        return data

    except requests.exceptions.ConnectionError as e:
        pass

def updateNews():
    for title, link in getNews():
        if link.startswith('https'):
            continue
        else:
            row = NewsDb.query.filter_by(title=title,link=link).first()
            if row is not None:
                continue
            else:
                row1 = NewsDb(title=title,link=link)
                db.session.add(row1)
    db.session.commit()


def main():
    pass

if __name__ == '__main__':
    main()
