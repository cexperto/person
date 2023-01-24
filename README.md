
# Person API

This API allow crud with Person module

## Deployment

To deploy this project, ther are 2 options: Manually, cli:

Manually:


venv in linux (make sure have root permissions):

    sudo apt install python3-virtualenv python3-venv
    virtualenv -p `which python3` venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    python3 manage.py makemigrations customuser
    python3 manage.py migrate
    python3 manage.py runserver


venv in windows:

    python -m venv venv
    source venv/scripts/activate
    pip install -r requirements.txt
    python manage.py makemigrations customuser
    python manage.py migrate
    python manage.py runserver


With cli:

run:

linux:

    chmod u+x clili
    ./clili

windows:

    chmod u+x cliwin
    ./cliwin


## API Reference

base url: 

https://person-production.up.railway.app/

base local url:

http://127.0.0.1:8000/


#### Get all items

```http
  GET /person/
```
Response 
status 200

#### Register item

```http
  POST /person/
```
Json exaple:

    {     
        "document_type": "cedula",
        "document": "123456789",
        "first_name": "user",
        "last_name": "user user",
        "email": "user@mail.com",
        "hobbie": "play"
    }
Response

status 201


#### Update item

```http
  PUT /person/<int>/
```
Json exaple:

    {     
        "document_type": "cedula",
        "document": "123456789",
        "first_name": "hey",
        "last_name": "user user",
        "email": "user@mail.com",
        "hobbie": "play"
    }
Response

status 200

#### Update partil item

```http
  PATCH /person/<int>/
```
Json exaple:

    {   
        "document": "123456789"
    }
Response

status 200

#### Delete item

```http
  DELETE /person/<int>/
```

Response

status 204


Run tests:

run:

Windows:

    python manage.py test

Linux:

    python3 manage.py test
