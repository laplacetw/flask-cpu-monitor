#!/usr/bin/env python3
# coding:utf-8

import sqlite3, time


def connect():
    conn = sqlite3.connect('data.db', check_same_thread=False)
    print(">>> Database Connect")
    return conn


def cpu_recorder(conn, data):
	keys = list(data.keys()) 
	keys.sort()
	conn.execute('begin')  # start SQLite transaction
	for key in keys:
		row = data[key].split(",")
		ip, cpu, memory, date = key, row[0], row[1], row[2]
		conn.execute("INSERT INTO CPU (ip, cpu, memory, date) VALUES(?, ?, ?, ?)", (ip, cpu, memory, date))
	
	conn.commit()  # end SQLite transaction


# query the latest data
def select_cpu(conn, ip):
	res = conn.execute("SELECT * FROM CPU WHERE ip=(?) ORDER BY id DESC LIMIT 8", (ip,))
	res = res.fetchall()
	res = str(res).replace(' ', '').replace('(', '').replace('[', '').replace(']', '').split('),')
	res[len(res) - 1] = res[len(res) - 1].replace(')', '')
	res = res[: :-1]
	return res  # e.g. ["6,'192.168.0.23',18.5,38.6,'2019-07-08T16:30:00'", "5,..."]


def select(conn):
    res = conn.execute("SELECT date, ip, cpu, memory FROM CPU")
    return res