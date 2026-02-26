#데이터 분석

import pandas as pd

df = pd.read_csv("air_data.csv")

# 기본 정보 확인
print("=== 데이터 크기 ===")
print(df.shape)

print("\n=== 컬럼 목록 ===")
print(df.columns.tolist())

print("\n=== 기본 통계 ===")
print(df[["pm10Value", "pm25Value", "o3Value", "no2Value"]].describe())

print("\n=== 진주 측정소만 보기 ===")
jinju = df[df["stationName"].str.contains("진주|상대|정촌|명서", na=False)]
print(jinju[["stationName", "pm10Value", "pm25Value", "khaiValue"]])