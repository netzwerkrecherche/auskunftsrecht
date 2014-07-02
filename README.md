# Auskunftsrecht - Suche über Urteile zum Landespressegesetz

## Setup

    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py extract_rulings <csv file> <directory with pdfs> > urteile.json # optional
    python manage.py import_rulings urteile.json
    python manage.py rebuild_index
    python manage.py runserver

## Deployment

    # Setup Heroku
    # Add postgres and bonsai search add-ons
    heroku config:set DJANGO_SECRET_KEY=<your secret key>
    git push heroku master
