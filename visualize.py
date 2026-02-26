#데이터 시각화

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 한글 폰트 설정 (Mac)
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("air_data.csv")

# 숫자로 변환
df["pm10Value"] = pd.to_numeric(df["pm10Value"], errors="coerce")
df["pm25Value"] = pd.to_numeric(df["pm25Value"], errors="coerce")
df["khaiValue"] = pd.to_numeric(df["khaiValue"], errors="coerce")

# 진주 측정소만
jinju = df[df["stationName"].str.contains("진주|상대|정촌|명서", na=False)]

# 그래프
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("진주 대기오염 현황", fontsize=16, fontweight="bold")

# PM10 막대그래프
axes[0].bar(jinju["stationName"], jinju["pm10Value"], color=["#7c6af7", "#48f7b8", "#f7c948"])
axes[0].set_title("PM10 미세먼지")
axes[0].set_ylabel("㎍/㎥")

# 통합대기환경지수
axes[1].bar(jinju["stationName"], jinju["khaiValue"], color=["#7c6af7", "#48f7b8", "#f7c948"])
axes[1].set_title("통합대기환경지수 (KHAI)")
axes[1].set_ylabel("지수")

plt.tight_layout()
plt.savefig("jinju_air_chart.png", dpi=150)
plt.show()
print("✅ 차트 저장 완료!")