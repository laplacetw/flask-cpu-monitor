
#1 初始化需先執行create_database.py建立資料庫，並確認防火牆輸入/輸出允許python.exe通行

#2 app.py為Server主程式，可直接開啟運行，勿重複執行

#3 監控網址為http://{ServerIP}:8080

#4 Server每10分鐘紀錄 CPU & RAM 使用率

#5 監控腳本每10秒向Server發送受監控主機之 CPU & RAM 使用率

#6 監控畫面每10秒更新 CPU & RAM 使用率 / 每5分鐘更新 Line Chart

#7 執行export.py可輸入日期區間來匯出資料庫中的數據為.csv檔