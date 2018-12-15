# -*- coding: UTF-8 -*-
import schedule
import requests
import login
import settings

# api = 'https://c.liepin.com/resume/refreshresume.json'
params = {
    "res_id_encode": settings.res_id_encode,
    "traceId": "46164588833"
}


def job():
    print("I'm working...")
    cookies = login.login()
    print cookies
    new_headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookies
    }
    try:
        r = requests.post(settings.refresh_api, data=params, headers=new_headers)
        print(r.text)
    except IOError:
        print 'error'


schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
