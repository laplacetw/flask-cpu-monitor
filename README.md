![](https://img.shields.io/github/license/laplacetw/flask-cpu-monitor?style=flat-square)
# flask-cpu-monitor
A simple cpu monitor on web  built by Flask for local area network.
<br>
Testing Environment :
- OS : Windows 10
- Python : python-3.7.2-amd64

Click the image below to watch video demo :
<br><br>
[![DEMO](https://raw.githubusercontent.com/laplacetw/flask-cpu-monitor/master/demo_02.png)](https://www.youtube.com/watch?v=qZ12nJMpYvA)

## Server
- The monitor page will run at {server host}:8080.
- Running log file will be saved under Server root folder.
- Usage data will be recorded in SQLite by Server every 10 min.
- CPU/RAM usage data will be updated every 10 sec.
- Line chart will be updated every 5 min.
- We can get a .csv file about usage data by executing export.py file under Server root folder.

## Client
- We should modify the parameter about host in client script before running.
- The client script will send usage data by POST every 10 sec.

## Installation
1. Download and unzip the ZIP file, then install Server/Client packages offline on computers in local area network.
2. Copy CPU_Monitor folder under Server root folder to your server host, and CPU_Monitor_client.py file to computers you want to monitor.
3. Execute the create_database.py file under Server root folder.
4. Run the server and client, that's all.

## Line Chart
Powered by [ApexCharts](https://apexcharts.com).
