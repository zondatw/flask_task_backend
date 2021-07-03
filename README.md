# Flask task backend

## Prerequisites

Create .env file  

example:  

```
FLASK_APP=main
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/ExerciseDB
```

## Docker

Create Mysql from Docker-compose file  

```bash
$ docker-compose up
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

## Reference

[cookiecutter-flask](https://github.com/cookiecutter-flask)  
