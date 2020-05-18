import time
from datetime import datetime as dt

hosts = r"hosts.txt.txt"
redirect = "127.0.0.1"
site_list=["www.facebook.com","www.instagram.com","www.reddit.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23,59):
        print("yes")
        with open(hosts,'r+') as file:
            content = file.read()
            for site in site_list:
                if site in content:
                    pass
                else:
                    file.write(redirect + "  " + site +"\n")

    else:
        with open(hosts,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in site_list ):
                    file.write(line)
            file.truncate()
        print("no")

    time.sleep(5)
