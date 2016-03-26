FROM python-base

# start supervisor to run our wsgi server
RUN git clone https://github.com/wg/wrk.git
WORKDIR wrk
RUN make
# Should check url in docker-machine ip and docker ps -> ports
RUN ./wrk -t12 -c400 -d30s http://192.168.99.100:32780/
