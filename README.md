# DesignHunt Django API App

This is an DesignHunt Django app that convert data into restfull APIs

**This example is written with Django 2.1.

You can view a working version of this app
[here](http://exaple.com).
Running this app on your local machine in development will work as
well.

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ ./dev.env.sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use gunicorn to run the server locally (after copying
`dev.env.sh` to `.env.sh`):


## Deploy to Production

Run the following commands to deploy the app to Server:

```sh
$ git clone https://github.com/django.git
$ python manage.py migrate
$ cd DesignHunt
$ ./path/to/.env.sh
$ gunicorn -b 0.0.0.0:8000 DesignHunt.wsgi
```

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/issues).

Master [git repository](http://github.com/django):

* `git clone git://github.com/django`
