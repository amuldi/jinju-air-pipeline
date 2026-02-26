# 데이터 수집

import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

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
print(response.status_code)
print(response.text)
data = response.json()

items = data["response"]["body"]["items"]
df = pd.DataFrame(items)
print(df.head())

df.to_csv("air_data.csv", index=False)
print("✅ 저장 완료!")