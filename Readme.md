Kako zagnati aplikacijo na Macu?

- prvi pogoj je, da ima uporabnik na računalniku naložen python 3 in orodje pip

1. pipenv install django
2. pipenv shell
3. pip3 install -r requirements.txt
4. python manage.py runserver

Če je podatkovna baza izbrisana, mora uporabnik izvesti naslednja ukaza:

5. python manage.py makemigrations
6. python manage.py migrate
