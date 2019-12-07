from django_cron import CronJobBase, Schedule
from bs4 import BeautifulSoup
import requests
from news.models import News
import time
from crawler.settings import site_url


def scrape(url):
    try:
        resp = requests.get(url)
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
        time.sleep(1)


class ScraperJob(CronJobBase):
    RUN_EVERY_MINS = 30  # every 30 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'crop_app.my_cron_job'

    def do(self):
        scrape(site_url)


