#데이터 자동 수집

import schedule
import time
import requests
import pandas as pd
import sqlite3
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")

def collect_and_save():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 데이터 수집 시작...")

    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    params = {
        "serviceKey": API_KEY,
        "returnType": "json",
        "numOfRows": 100,
        "pageNo": 1,
        "sidoName": "경남",
        "ver": "1.0"
    }

    response = requests.get(url, params=params)
    items = response.json()["response"]["body"]["items"]
    df = pd.DataFrame(items)

    for col in ["pm10Value", "pm25Value", "o3Value", "no2Value", "khaiValue"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["savedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("air_data.db")
    df[["stationName","pm10Value","pm25Value","o3Value","no2Value","khaiValue","dataTime","savedAt"]].to_sql(
        "air_pollution", conn, if_exists="append", index=False
    )
    conn.close()

    print(f"✅ {len(df)}개 측정소 데이터 저장 완료!")

# 매일 오전 9시에 자동 실행
schedule.every().day.at("09:00").do(collect_and_save)

# 테스트용 — 지금 당장 한 번 실행
collect_and_save()

print("\n⏰ 스케줄러 실행 중... (Ctrl+C로 종료)")
while True:
    schedule.run_pending()
    time.sleep(60)