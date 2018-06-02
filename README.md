# django-vue-aiohttp

An experimental WIP that uses django, vue and aiohttp-wsgi to serve and also 
allow for django websockets/event handlers.

Whitenoise is used for serving static files.

# usage

For local dev setup virtual enviro (I use pipenv personally but here is the usual pip) then:

```
pip install -r requirements
npm install
```
Then in one terminal
```
npm run dev
```
And in another
```
python run.py
```

Then when you are ready to build:

```
npm set progress=false && npm install -s --no-progress && npm run build
python manage.py collectstatic --noinput
```

# Inspiration/libraries

* https://github.com/NdagiStanley/vue-django
* https://github.com/ariera/django-vue-template
* https://github.com/etianen/aiohttp-wsgi
* https://github.com/aio-libs/aiohttp-sse
* https://github.com/arteria/django-favicon-plus
* http://whitenoise.evans.io/
