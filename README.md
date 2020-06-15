# logbook

1. Python 3.x & git installieren
2. `git clone https://github.com/seike87/logbook`
3. In den Ordner logbook wechseln und eine virtuelle Umgebung für Python erstellen: `python3 -m venv myvenv`
4. Sicherstellen, dass Python in der virtuellen Umgebung ist: `source myvenv/bin/activate`
5. pip upgraden `python -m pip install --upgrade pip`
6. Django installieren `pip install -r requirements.txt`
7. SQLite DB erstellen `python manage.py makemigrations` UND `python manage.py migrate`
8. Adminkonto für das Backend einrichten (Dialog im Terminal befolgen) `python manage.py createsuperuser`
9. Für die Installation von nginx und gunicorn am besten folgende Anleitung lesen (basiert auf Debian 9; ab Schritt 4): https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-debian-9
10. Das Backend lässt sich über https://meine.domain/admin aufrufen, dort lassen sich dann auch weitere Accounts hinzufügen, die dann bspw auf die Einträge und die Downloadfunktion zurückgreifen können
