help:
	@echo "run-test - Run container test benchmark for in local mode"
run-test:
	docker run django_web /code/wrk/wrk -t12 -c400 -d30s http://192.168.99.100:8000/