## Commands

### Remove a file from the repo
```
git rm --cached <file name>
```

### Create virtual environment
```
python -m venv <virtual env name>
```

### Check packages that are intalled in the virtual environment

You can copy that list of packages and dump it in the `requirements.txt`
```
pip freeze
```

### Activate virtual environment
Windows
```
<virtual env name>\Scripts\activate
```

Linux or Mac
```
source <virtual env name>/bin/activate
```

### Create Django project
```
django-admin startproject <project name>
```

### Create apps inside the project
Make sure you are inside the project folder

```
python manage.py startapp <app name>
```

### Run the server for the project
```
python manage.py runserver
```

### Run migrations for the project
Make sure you are inside the project folder

```
python manage.py migrate
```

### Create super user for the admin panel
Make sure you are inside the project folder

```
python manage.py createsuperuser
```

### Create migrations when changing models in the app
Make sure you are inside the project folder

```
python manage.py makemigrations
```
