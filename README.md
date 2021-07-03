# Flask task backend

## Prerequisites

### Local

Create .env file  

example:  

```text
FLASK_APP=main
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/ExerciseDB
```

### Docker dev

Create .env.dev file  

example:  

```text
FLASK_APP=main
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://root:password@db:3306/ExerciseDB
```

### Docker test

Create .env.test file  

example:  

```text
FLASK_APP=main
FLASK_ENV=test
DATABASE_URL=mysql+pymysql://root:password@testdb:3306/TestDB
```

### Docker prod

Create .env.pod file  

example:  

```text
FLASK_APP=main
FLASK_ENV=production
DATABASE_URL=mysql+pymysql://root:password@db:3306/ExerciseDB
```

## Docker

### Dev

```bash
# start
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up
# close
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml down
```

### Test

```bash
# start
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml -f docker-compose.test.yaml up
# close
$ docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml -f docker-compose.test.yaml down
```

### Prod

```bash
# start
$ docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml up
# close
$ docker-compose -f docker-compose.yaml -f docker-compose.prod.yaml down
```

### Makefile

```bash
# start dev
$ make dev

# start test
$ make test

# start prod
$ make prod

# stop
$ make clean
```

### Run test in docker compose (Test)

```shell
$ docker exec -it {project name}_backend_1 /bin/bash
root@xxxxxxxxxx:/project# poetry run flask test
```


## Flask command

### Run

```bash
$ flask run
```

[http://127.0.0.1:5000](http://127.0.0.1:5000)  

### Test

```bash
$ flask test
```

### DB

```bash
# Generate migrations file
$ flask db migrate
# Migrate db
$ flask db upgrade
```

## Poetry

```bash
# install dependencies
$ poetry install
# run shell
$ poetry shell
```

## Reference

[cookiecutter-flask](https://github.com/cookiecutter-flask)  
