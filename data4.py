import streamlit as st
from streamlit_ace import st_ace

def show():
    st.title("4차시 - 피보나치 수열과 함수")

    st.markdown("""
    ### 📌 학습 목표
    - 함수를 정의하고 사용할 수 있다.
    - 피보나치 수열을 함수로 구현할 수 있다.

    ---

    ### 🧠 실습 과제
    - 항 개수를 입력받아 피보나치 수열을 생성하는 함수를 만들어보세요.
    """)

    default_code = """def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

sequence = fibonacci(10)
st.write("피보나치 수열:", sequence)
"""

    user_code = st_ace(
        language="python",
        theme="monokai",
        value=default_code,
        height=220,
        key="lesson4_editor"
    )

    if st.button("코드 실행하기"):
        try:
            exec(user_code, {"st": st})
        except Exception as e:
            st.error(f"❌ 실행 중 오류: {e}")