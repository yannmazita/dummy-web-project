# Installation
## Using Poetry
In project root:
```commandline
poetry install && cd front; poetry shell && npm install; cd ../
```
## Using requirements.txt
Dependencies defined in requirements.txt can be installed in a virtual environment.
```commandline
pip install -r requirements.txt
```

# Running
## Backend
In project root:
```commandline
cd back; poetry shell && python manage populate_server && python manage.py migrate && python manage.py runserver
```
Backend will be accessible at localhost:8000
## Frontend
In project root:
```commandline
cd front; poetry shell && npm install && npm run serve
```
Frontend will be accessible at localhost:8080

# Disclaimer
Documentation may severely lag behind actual features as I learn vuejs.
