#데이터 베이스 저장

import sqlite3
import pandas as pd
from datetime import datetime

# DB 연결 (없으면 자동 생성)
conn = sqlite3.connect("air_data.db")
cursor = conn.cursor()

# 테이블 만들기
cursor.execute("""
    CREATE TABLE IF NOT EXISTS air_pollution (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stationName TEXT,
        pm10Value REAL,
        pm25Value REAL,
        o3Value REAL,
        no2Value REAL,
        khaiValue REAL,
        dataTime TEXT,
        savedAt TEXT
    )
""")

# CSV 데이터 불러오기
df = pd.read_csv("air_data.csv")

# 숫자 변환
for col in ["pm10Value", "pm25Value", "o3Value", "no2Value", "khaiValue"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# DB에 저장
df["savedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df[["stationName","pm10Value","pm25Value","o3Value","no2Value","khaiValue","dataTime","savedAt"]].to_sql(
    "air_pollution", conn, if_exists="append", index=False
)

# 확인
print("=== DB 저장 완료 ===")
result = pd.read_sql("SELECT * FROM air_pollution LIMIT 5", conn)
print(result)

conn.close()