.PHONY: docs

build:
	docker-compose build

rebuild:
	docker-compose build --force-rm

start:
	docker-compose up -d web

stop:
	docker-compose down

stop-clean: ## stops, rms containers, images and volumes
	docker-compose down --rmi all -v --remove-orphans

clean:
	rm -rf .pytest_cache
