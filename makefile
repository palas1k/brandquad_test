include .env

build:
	docker compose build web

run: build
	docker compose up --remove-orphans -d
