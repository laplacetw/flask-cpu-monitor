#!/usr/bin/env python3
# coding:utf-8

import sqlite3, time


def main():
    conn = sqlite3.connect('data.db')

    print(">>> Database data.db created successfully.")
    time.sleep(2)

    conn.execute("CREATE TABLE IF NOT EXISTS CPU (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ip TEXT, cpu REAL, memory REAL, date TEXT)")
    print(">>> Table CPU created successfully.")
    
    conn.close()
    input(">>> Pls close the current window.")


if __name__ == '__main__':
    main()