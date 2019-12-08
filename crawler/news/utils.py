from bs4 import BeautifulSoup
import requests
from crawler.news.models import News
import time
from crawler.crawler.settings import site_url


def scrape():
    try:
        resp = requests.get(site_url)
    except:
        return

    page = resp.content

    soup = BeautifulSoup(page,
                         features='lxml')

    elems = soup.find_all('tr', attrs={'class': 'athing'})

    for i, el in enumerate(elems):
        a = el.find('a', attrs={'class': 'storylink'})
        url = a['href']
        title = a.text
        News.objects.create(
            title=title,
            url=url,
        )
        print(i, a)
        # time.sleep(1)
