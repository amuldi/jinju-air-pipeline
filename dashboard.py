# 터미널 -> 웹 대시보드로 시각화

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="진주 대기오염 대시보드", page_icon="🌬️", layout="wide")

st.title("경남 대기오염 모니터링")
st.caption("공공데이터 API 기반 실시간 대기오염 현황")

# 데이터 불러오기
conn = sqlite3.connect("air_data.db")
df = pd.read_sql("SELECT * FROM air_pollution", conn)
conn.close()

# 최신 데이터만
latest_time = df["dataTime"].max()
latest = df[df["dataTime"] == latest_time]

# 상단 지표
st.subheader(f"최신 수집 시간: {latest_time}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("PM10 평균", f"{latest['pm10Value'].mean():.1f} ㎍/㎥")
col2.metric("PM2.5 평균", f"{latest['pm25Value'].mean():.1f} ㎍/㎥")
col3.metric("대기지수 평균", f"{latest['khaiValue'].mean():.1f}")
col4.metric("측정소 수", f"{len(latest)}개")

st.divider()

# 진주 측정소 따로 보기
st.subheader("📍 진주 측정소 현황")
jinju = df[df["stationName"].str.contains("진주|상대|정촌|명서", na=False)]

if not jinju.empty:
    fig1 = px.bar(
        jinju[jinju["dataTime"] == latest_time],
        x="stationName", y="pm10Value",
        color="pm10Value", color_continuous_scale="RdYlGn_r",
        title="진주 측정소별 PM10",
        labels={"stationName": "측정소", "pm10Value": "PM10 (㎍/㎥)"}
    )
    st.plotly_chart(fig1, use_container_width=True)

st.divider()

# 시간대별 변화 (쌓인 데이터)
st.subheader("📈 시간대별 PM10 변화 (진주)")
if len(jinju["dataTime"].unique()) > 1:
    jinju_trend = jinju.groupby("dataTime")["pm10Value"].mean().reset_index()
    fig2 = px.line(
        jinju_trend, x="dataTime", y="pm10Value",
        title="진주 PM10 시간대별 평균",
        labels={"dataTime": "시간", "pm10Value": "PM10 평균 (㎍/㎥)"}
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("📊 데이터가 더 쌓이면 시간대별 그래프가 나타나요! (현재 수집 횟수 부족)")

st.divider()

# 전체 측정소 랭킹
st.subheader("🏆 경남 PM10 TOP 10")
top10 = latest.nlargest(10, "pm10Value")[["stationName", "pm10Value", "pm25Value", "khaiValue"]]
top10.columns = ["측정소", "PM10", "PM2.5", "대기지수"]
st.dataframe(top10, use_container_width=True)