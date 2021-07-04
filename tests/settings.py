from environs import Env

env = Env()
env.read_env()


ENV = "Test"
TESTING = True
DEBUG = True
SQLALCHEMY_DATABASE_URI = env.str("TEST_DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False