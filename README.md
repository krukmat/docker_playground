Docker Playground
=================

 - First intention was to create a toolbox to benchmark different python based framework such as Django (with channels) vs AioHttp.
 - Also I was playing around with docker, docker-composer world.

aiohttp_composer:
    docker-compose up
django:
    docker-compose run web django-admin.py startproject composeexample . # Create the project 1st time only
    docker-compose up
aiohttp:
    make build-local
    make run-local
    make help