help:
	@echo "build-local - Build container for local development"
	@echo "build-deploy - Build container in production mode"
	@echo "run-local - Run container for local development"
	@echo "run-deploy - Run container for in production mode"
	@echo "run-test - Run container test benchmark for in local mode"

build-base:
	cd ops/base/; docker build -t="python-base" .

build-local: build-base
	cd ops/local/; docker build -t="python-local" .

build-deploy: build-base
	cd ops/deploy/; docker build -t="python-deploy" .

build-test: build-base
	cd ops/test/; docker build -t="python-test" .

run-local: build-local
	docker run -P -t -i -v $(CURDIR)/app:/opt/app python-local

run-deploy: build-deploy
	docker run -P -t -i -v $(CURDIR)/app:/opt/app python-deploy

run-test: build-test
	docker run -P -t -i -v $(CURDIR)/app:/opt/app python-test
