#SQL 쿼리로 데이터 조회

import sqlite3
import pandas as pd

conn = sqlite3.connect("air_data.db")

# 1. 미세먼지 TOP 5 측정소
print("=== PM10 높은 순 TOP 5 ===")
df1 = pd.read_sql("""
    SELECT stationName, pm10Value, pm25Value
    FROM air_pollution
    ORDER BY pm10Value DESC
    LIMIT 5
""", conn)
print(df1)

# 2. 진주 측정소만
print("\n=== 진주 측정소 ===")
df2 = pd.read_sql("""
    SELECT stationName, pm10Value, pm25Value, khaiValue
    FROM air_pollution
    WHERE stationName LIKE '%진주%'
       OR stationName IN ('상대동(진주)', '정촌면', '명서동')
""", conn)
print(df2)

# 3. 전체 평균
print("\n=== 경남 전체 평균 ===")
df3 = pd.read_sql("""
    SELECT 
        ROUND(AVG(pm10Value), 1) as pm10평균,
        ROUND(AVG(pm25Value), 1) as pm25평균,
        ROUND(AVG(khaiValue), 1) as 대기지수평균
    FROM air_pollution
""", conn)
print(df3)

conn.close()