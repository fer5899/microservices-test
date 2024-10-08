DATA = /home/fer5899/data
WP_DATA = $(DATA)/wordpress
DB_DATA = $(DATA)/mariadb

all: up

build:
	docker compose -f ./srcs/docker-compose.yml build

up: build
	@mkdir -p $(WP_DATA)
	@mkdir -p $(DB_DATA)
	docker compose -f ./srcs/docker-compose.yml up -d

stop:
	docker compose -f ./srcs/docker-compose.yml stop

start:
	docker compose -f ./srcs/docker-compose.yml start

down:
	docker compose -f ./srcs/docker-compose.yml down

fclean:
	docker compose -f ./srcs/docker-compose.yml down -v --rmi all --remove-orphans
	docker system prune -a --volumes -f
	rm -rf $(DATA)

logs:
	

re: fclean up
	

.PHONY: build up all stop start down fclean re
