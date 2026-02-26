# 🌬️ 경남 대기오염 실시간 모니터링 파이프라인

공공데이터 API를 활용해 경남 지역 대기오염 데이터를 자동 수집하고, SQLite DB에 저장하여 Streamlit 웹 대시보드로 시각화하는 데이터 파이프라인 프로젝트입니다.

![Python](https://img.shields.io/badge/Python-3.13-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red) ![SQLite](https://img.shields.io/badge/SQLite-3-green)

---

## 📌 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 데이터 소스 | 한국환경공단 에어코리아 대기오염정보 API |
| 수집 지역 | 경남 전체 (50개 측정소) |
| 수집 주기 | 매일 오전 9시 자동 수집 |
| 저장 방식 | SQLite DB (데이터 누적 저장) |
| 시각화 | Streamlit 웹 대시보드 |

---

## 🏗️ 아키텍처

```
공공데이터 API
      ↓
collect.py (데이터 수집)
      ↓
air_data.csv / air_data.db (저장)
      ↓
analyze.py    → 터미널 분석
visualize.py  → 차트 이미지 저장
query.py      → SQL 질의
dashboard.py  → Streamlit 웹 대시보드
```

---

## 📁 파일 구조

```
jinju-air-pipeline/
├── collect.py       # 공공API 데이터 수집 → CSV 저장
├── analyze.py       # pandas 기반 데이터 분석
├── visualize.py     # matplotlib/seaborn 시각화
├── database.py      # SQLite DB 저장
├── query.py         # SQL 쿼리 분석
├── scheduler.py     # 자동 수집 스케줄러
├── dashboard.py     # Streamlit 웹 대시보드
├── .env             # API 키 (git 제외)
├── .gitignore
└── README.md
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
git clone https://github.com/amuldi/jinju-air-pipeline.git
cd jinju-air-pipeline
python3 -m venv venv
source venv/bin/activate
pip install requests pandas python-dotenv matplotlib seaborn streamlit plotly schedule
```

### 2. API 키 설정

[공공데이터포털](https://www.data.go.kr)에서 **한국환경공단_에어코리아_대기오염정보** API 키를 발급받고 `.env` 파일을 생성하세요.

```
API_KEY=발급받은_키_입력
```

### 3. 데이터 수집

```bash
python3 collect.py       # 1회 수집
python3 scheduler.py     # 매일 자동 수집
```

### 4. 대시보드 실행

```bash
streamlit run dashboard.py
```

브라우저에서 `http://localhost:8501` 접속

---

## 📊 주요 기능

- **실시간 데이터 수집** — 공공 API에서 경남 50개 측정소 대기오염 데이터 수집
- **자동 스케줄러** — 매일 오전 9시 자동 실행, SQLite DB에 누적 저장
- **SQL 분석** — PM10 TOP 5, 진주 측정소 필터링, 경남 평균 통계
- **웹 대시보드** — Streamlit + Plotly 기반 인터랙티브 시각화

---

## 🛠️ 사용 기술

- **언어**: Python 3.13
- **데이터 처리**: pandas, sqlite3
- **시각화**: matplotlib, seaborn, plotly
- **웹 대시보드**: Streamlit
- **자동화**: schedule
- **API**: 한국환경공단 에어코리아
