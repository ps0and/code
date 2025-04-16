import streamlit as st

# 페이지 제목
st.title("7days CODE")

# 드롭다운 옵션 설정
options = {
    "1day 파이썬 문법(1)": "data1",
    "2day 파이썬 문법(2)": "data2",
    "3day 파이썬 문법(3)": "data3",
    "4day 실습(1)": "data4",
    "5day 실습(2))": "data5",
    "6day 실습(3)": "data6",    
    "7day 실습(4)": "data7"
}

selection = st.selectbox("수업을 선택하세요:", list(options.keys()))

# 선택에 따른 해당 모듈 실행
if selection:
    module_name = options[selection]
    module = __import__(module_name)
    module.show()