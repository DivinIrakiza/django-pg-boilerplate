# django-pg-boilerplate
Minimal boilerplate code for DJANGO with Postgresql



## Setup

```bash
git clone https://github.com/DivinIrakiza/django-pg-boilerplate.git
cd django-pg-boilerplate/
```


### Linux
```bash
pip install virtualenv 
virtualenv env -p python3
source env/bin/activate
cd app/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Windows
```bash
pip install virtualenv 
py -m venv env
.\env\Scripts\activate
cd app/
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```