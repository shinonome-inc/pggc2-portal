# server

## setup

```sh
touch .env
docker volume create pggc-data
```

env file
```
DJANGO_SETTINGS_MODULE=config.settings.development
DJANGO_SECRET_KEY=hogehoge
GRPC_SERVER_URL=
SLACK_API_URL=
```

load initial data in docker container
```sh
python manage.py migrate
python manage.py loaddata --format=yaml fixtures/fixtures.yaml
```

coverage report (on app directory)
```sh
coverage run manage.py test --settings=config.settings.development
```