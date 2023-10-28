# Installation (poetry)
In project root:
```commandline
poetry install && cd front; npm install; cd ../
```

# Running
## Backend
In project root:
```commandline
cd back; python manage.py migrate && python manage.py runserver
```
Backend will be accessible at localhost:8000
## Frontend
In project root:
```commandline
cd front; npm run serve
```
Frontend will be accessible at localhost:8080

# Disclaimer
Documentation may severely lag behind actual features as I learn vuejs.
