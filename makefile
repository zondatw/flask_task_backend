DOCKERCMD = docker
COMPOSE_CMD = docker-compose

# docker compose
DOCK_COMPOSE_DEV_FILES = -f docker-compose.yaml -f docker-compose.dev.yaml
DOCK_COMPOSE_PROD_FILES = -f docker-compose.yaml -f docker-compose.prod.yaml

all: dev
dev:
	$(COMPOSE_CMD) $(DOCK_COMPOSE_DEV_FILES) build
	$(COMPOSE_CMD) $(DOCK_COMPOSE_DEV_FILES) up

prod:
	$(COMPOSE_CMD) $(DOCK_COMPOSE_PROD_FILES) build
	$(COMPOSE_CMD) $(DOCK_COMPOSE_PROD_FILES) up

.PHONY: clean
clean:
	$(COMPOSE_CMD) $(DOCK_COMPOSE_DEV_FILES) down
	$(COMPOSE_CMD) $(DOCK_COMPOSE_PROD_FILES) down
