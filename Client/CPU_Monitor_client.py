#!/usr/bin/env python3
# coding:utf-8
import sys, psutil, requests, time, datetime


delay = 10  # send cpu data every 10 seconds
host = '{your server host}:8080'  # sever host
ip, cpu, memory, date, url, data, res = "", "", "", "", "", "", ""


def main():
    while True:
        ip = psutil.net_if_addrs()['乙太網路'][1].address  # get IP address
        cpu =  psutil.cpu_percent()
        memory = psutil.virtual_memory()[2]
        date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # YYYY-MM-DDThh:mm:ss
        url = host + '/api'
        data = {
            'ip' : ip,
            'cpu' : cpu,
            'memory' : memory,
            'date' : date
        }
        try:
            res = requests.post(url=url, json=data)  # post
            if res.ok:
                print('POST OK!')
        except requests.exceptions.ConnectionError:
            print(">>> Server Connection Error")
        except:
            print(">>> ", sys.exc_info()[0])

        time.sleep(delay)  # delay


if __name__ == '__main__':
    main() 