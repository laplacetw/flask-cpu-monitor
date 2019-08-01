#!/usr/bin/env python3
# coding:utf-8

import atexit, psutil, time, logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from sqlite import *


app = Flask(__name__)
real_time = {}
conn = connect()  # db connection
scheduler = BackgroundScheduler()  # task scheduler
scheduler.add_job(cpu_recorder, args=[conn, real_time], trigger='interval', minutes=10)
scheduler.start()


# real time data collection
@app.route('/api', methods=['GET','POST'])
def api():
    if request.method == 'POST':
        try:
            data = request.json
            ip, cpu, memory, date = str(data['ip']), str(data['cpu']), str(data['memory']), data['date']
            real_time[ip] = cpu + "," + memory + "," + date
            return 'OK'
        except Exception as e:
            app.logger.error('%s', e)
    else:
        try:
            data = []
            keys = list(real_time.keys()) 
            keys.sort()
            for key in keys:
                 data.append(str(key) + "," + real_time[key])
            return jsonify(result={"status": 200}, data=data)
        except Exception as e:
            app.logger.error('%s', e)


# query the latest data
@app.route('/api/ip', methods=['GET'])
def api_ip():
    try:
        ip = request.args.get('no')
        data = select_cpu(conn, ip)
        return jsonify(result={"status": 200}, data=data)
    except Exception as e:
            app.logger.error('%s:' + ip, e)


# dashboard
@app.route('/', methods=['GET'])
def monitor():
    try:
        ip = psutil.net_if_addrs()['乙太網路'][1].address  # get IP address
        app.logger.info('Someone view the CPU Monitor')
        return render_template('dashboard.html', ip=ip)
    except Exception as e:
        app.logger.error('%s', e)


# when server shutdown
atexit.register(lambda: conn.close())  # close db connection
atexit.register(lambda: scheduler.shutdown(wait=False))  # stop task scheduler

if __name__ == "__main__":
    # logger setup
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('CPU_Monitor.log', maxBytes=10000000, backupCount=5)
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    ip = psutil.net_if_addrs()['乙太網路'][1].address  # get IP address
    app.run(host=ip, port='8080')