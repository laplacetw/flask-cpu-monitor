#!/usr/bin/env python3
# coding:utf-8

import csv, datetime
from sqlite import connect, select


def main():
	print("[Date Format : YYYYMMDD]")
	start = input("Start Date : ")
	end = input("End Date : ")

	start = datetime.datetime(int(start[:4]), int(start[4:6]), int(start[6:]), 1, 1)
	end = datetime.datetime(int(end[:4]), int(end[4:6]), int(end[6:]), 23, 59)

	conn = connect()  # db connection
	res = select(conn)  # get raw data
	table = [['Datetime', 'IP', 'CPU', 'RAM']]
	for row in res:
		date = row[0].split('T')[0].split('-')
		date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), 11, 11)
		if date > start and date < end: 
			table.append(row)

	with open('data.csv', 'w', newline='') as csvfile:  # export as data.csv
		writer = csv.writer(csvfile)
		writer.writerows(table)

	conn.close()  # close connection


if __name__ == '__main__':
	main()