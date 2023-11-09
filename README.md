# Installation
## Using Poetry
In project root:
```commandline
poetry install && cd front && poetry shell
```
```commandline
npm install
```
## Using requirements.txt
Dependencies defined in requirements.txt can be installed in a virtual environment.
```commandline
pip install -r requirements.txt && cd front && npm install && cd ../
```

# Running
## Backend
In project root, inside poetry env/virtual environment:
```commandline
cd back; poetry shell 
```
or any command activating your virtual environment inside the back folder.
First start:
```commandline
python manage.py makemigrations gestion_adherents && python manage.py migrate && python manage.py populate_database && python manage.py runserver
```
Subsequent starts only require:
```commandline
python manage.py runserver
```
Backend will be accessible at localhost:8000
## Frontend
In project root:
```commandline
cd front; poetry shell
```
or any command activating your virtual environment inside the front folder.
```commandline
npm run serve
```
Frontend will be accessible at localhost:8080

# Disclaimer
Documentation may severely lag behind actual features.
