# logbook

1. Python 3.x & git installieren
2. `git clone https://github.com/seike87/logbook`
3. In den Ordner logbook wechseln und eine virtuelle Umgebung für Python erstellen: `python3 -m venv myvenv`
4. Sicherstellen, dass Python in der virtuellen Umgebung ist: `source myvenv/bin/activate`
5. pip upgraden `python -m pip install --upgrade pip`
6. Django installieren `pip install -r requirements.txt`
7. SQLite DB erstellen `python manage.py makemigrations` UND `python manage.py migrate`
8. Adminkonto für das Backend einrichten (Dialog im Terminal befolgen) `python manage.py createsuperuser`
8a. Testen, ob die Seite bereits korrekt ausgeliefert werden kann `python manage.py runserver` 
9. Für die Installation von gunicorn zunächst das Packet per `pip` installieren => `pip install gunicorn` (hat den Vorteil, dass man jeweils die aktuellste Version von gunicorn bekommt, da es in den offiziellen Packetquellen zum Teil veraltet ist)
10. Test, ob gunicorn die Seite überhaupt ausliefern kann `gunicorn --bind 0.0.0.0:8000 logbook.wsgi` (analog zu 8a)
11. Ab hier die [Anleitung](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) befolgen (ab Punkt **Creating systemd Socket and Service Files for Gunicorn**)
12. Das Backend lässt sich über https://meine.domain/admin aufrufen, dort lassen sich dann auch weitere Accounts hinzufügen, die dann bspw auf die Einträge und die Downloadfunktion zurückgreifen können
