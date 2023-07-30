## LAB -  Class 34
### Project: Django Template (salmon cookies)
### Author: Slava Makeev


### Setup
> Activate your virtual environment:
- $source venv/bin/activate
> Make sure to install apply dependencies locally:
- $pip install -r requirements.txt

### Docker setup:

- <http://localhost:8000>

- $`docker compose up --build`
- $`docker compose run web python3 manage.py makemigrations`
- $`docker compose run web python3 manage.py migrate`

- $`docker compose run web python manage.py collectstatic`
> Make sure your .env file contains your password and key

### To run docker use: 
$`docker compose run web`
### Database info:
- database hosting: <https://elephantsql.com/>
>Superuser
- username: admin
- password: 1234