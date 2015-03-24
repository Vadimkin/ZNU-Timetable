# ZNU-Timetable

Site with university timetable and REST API service for applications

## Installation

Clone the repository and install dependencies.

```
git clone https://github.com/Vadimkin/ZNU-Timetable.git
cd ZNU-Timetable
pip install -r requirements.txt
```

Then rename config file and set up config to db

```
cd znu
mv settings_secret.py.EXAMPLE settings_secret.py
nano settings_secret.py
```

## Run server

Database sync

```
python manage.py syncdb
```

Server running with command

```
python manage.py runserver
```
