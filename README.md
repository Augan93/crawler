"# crawler" 
Web Scraper Hacker News

Web scraper launches every 30 min.

**Инструкция по запуске:**

docker-compose build

docker-compose run --rm djangoapp /bin/bash -c "cd crawler; python manage.py migrate"

docker-compose run --rm djangoapp /bin/bash -c "cd crawler; python manage.py createsuperuser"

docker-compose run --rm djangoapp /bin/bash -c "cd crawler; python manage.py collectstatic"

docker-compose up

docker-compose down

