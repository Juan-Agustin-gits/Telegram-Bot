import datetime

def time_relationShip():
    now = datetime.datetime.now()
    init_relationShip = datetime.datetime(2024, 7, 26, 16, 30)
    time_relationShip = now - init_relationShip
    return time_relationShip
