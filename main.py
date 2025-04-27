import streamlit as st

# 페이지 제목
st.title(":rainbow[7days of Coding Mathematics]")
# 드롭다운 옵션 설정
options = {
    "1Day": "data1",
    "2Day": "data2",
    "3Day": "data3",
    "4Day": "data4",
    "5Day": "data5",
    "6Day": "data6",    
    "7Day": "data7"
}

selection = st.selectbox("도전을 시작합시다! 수업을 선택하세요. 👇", list(options.keys()))

# 선택에 따른 해당 모듈 실행
if selection:
    module_name = options[selection]
    module = __import__(module_name)
    module.show()