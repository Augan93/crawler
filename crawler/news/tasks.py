from crawler.celery import app
# from crawler.crawler.news.utils import scrape

from bs4 import BeautifulSoup
import requests
from .models import News

# from crawler.crawler.settings import site_url

site_url = 'https://news.ycombinator.com/'


def scrape():
    try:
        resp = requests.get(site_url)
    except:
        return

    if resp.status_code == 200:
        page = resp.content

        soup = BeautifulSoup(page,
                             features='lxml')

        elems = soup.find_all('tr', attrs={'class': 'athing'})

        for i, el in enumerate(elems):
            a = el.find('a', attrs={'class': 'storylink'})
            url = a['href']
            title = a.text

            try:
                News.objects.get(url=url)
            except News.DoesNotExist:
                News.objects.create(
                    title=title,
                    url=url,
                )

            print(i, a)


@app.task
def get_news():
    scrape()
    print("Hello there!")
