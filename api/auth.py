import api.config as config
import robin_stocks as r


def login():
  username = config.username
  password = config.password
  r.login(username,password)