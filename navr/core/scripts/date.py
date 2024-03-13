import datetime
def den_name():
    now = datetime.datetime.now()
    print(now.strftime("%A"))
    den = now.strftime("%A")
    return den
