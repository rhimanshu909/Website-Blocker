import time
from datetime import datetime as dt

hosts_path =r"/etc/hosts"
redirect="127.0.0.1"        #ipv4
redirect1="fe80::1%lo0"     #ipv6
website_list=["www.facebook.com","facebook.com","login.facebook.com","www.login.facebook.com","fbcdn.net","www.fbcdn.net","fbcdn.com","www.fbcdn.com","static.ak.fbcdn.net","static.ak.connect.facebook.com","connect.facebook.net","www.connect.facebook.net","apps.facebook.com"]

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18)):
        print('working hours...')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n'+redirect1+' '+website+'\n')
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print('You can enjoy now...')
    time.sleep(5)
