# Virchurro

A Python 3 Flask application built to spread the cinnamon sugary goodness of churros.
The app uses a single Postgresql table to store a map from random hashes to
"virtual churro" descriptions (so far, the description is only what song to play).

The available routes are:

Endpoint | Purpose                               | Method
---------|---------------------------------------|-------
`/`      | Index w/ form to create new Virturros | `GET`
`/<slug>`| View a Virchurro                      | `GET`
`/new`   | Create a new Virturro                 | `POST` (song=...)

## Install
1. `git clone...`
2. `cd virchurro`
3. `virtualenv venv && . venv/bin/activate`
4. `pip install -r requirements.txt`
5. Create a Postgresql database named `virchurro`
6. `python`
7. `from virchurro import db`
8. `db.create_all()`
9. `foreman start`

## Heroku
1. `heroku create`
2. Enable Postgresql
3. `git push heroku master`
4. `heroku run python`
5. `from virchurro import db`
6. `db.create_all()`
7. `heroku open`
