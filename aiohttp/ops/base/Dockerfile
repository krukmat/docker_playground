FROM ubuntu:14.04
MAINTAINER Matias Kruk <kruk.matias@gmail.com>

# keep upstart quiet
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# no tty
ENV DEBIAN_FRONTEND noninteractive

# get up to date
RUN apt-get update --fix-missing

# global installs [applies to all envs!]
RUN apt-get install -y build-essential git
RUN apt-get install -y python3.4 python3-pip
RUN apt-get install -y python-virtualenv
RUN apt-get install -y postgresql-9.3 postgresql-server-dev-9.3
RUN apt-get install -y nginx supervisor

# stop supervisor service as we'll run it manually
RUN service supervisor stop

# build dependencies for postgres and image bindings
RUN apt-get build-dep -y python-imaging python-psycopg2

# create a virtual environment and install all dependecies from pypi
RUN virtualenv /opt/venv
ADD ./requirements.txt /opt/venv/requirements.txt
RUN pip3 install -r /opt/venv/requirements.txt

# expose port(s)
EXPOSE 80
