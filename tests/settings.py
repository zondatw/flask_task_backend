from environs import Env

env = Env()
env.read_env()


ENV = "Test"
DEBUG = True
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False