"# crawler" 

docker-compose run --rm djangoapp /bin/bash -c "cd crawler; python manage.py migrate"
docker-compose run --rm djangoapp /bin/bash -c "cd crawler; python manage.py createsuperuser"


docker-compose run --rm djangoapp /bin/bash -c "cd crawler; python manage.py collectstatic"

docker-compose up

docker-compose down

