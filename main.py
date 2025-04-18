import streamlit as st

# 페이지 제목
st.title("7days of Coding Mathematics")
# 드롭다운 옵션 설정
options = {
    "1day": "data1",
    "2day": "data2",
    "3day": "data3",
    "4day": "data4",
    "5day": "data5",
    "6day": "data6",    
    "7day": "data7"
}

selection = st.selectbox("도전을 시작합시다! 수업을 선택하세요. 👇", list(options.keys()))

# 선택에 따른 해당 모듈 실행
if selection:
    module_name = options[selection]
    module = __import__(module_name)
    module.show()