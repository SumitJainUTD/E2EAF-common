import datetime
from time import sleep


def get_random_string():
    sleep(1)
    return str(datetime.datetime.now())\
        .replace("-", "")\
        .replace(" ", "")\
        .replace(":", "").split(".")[0]