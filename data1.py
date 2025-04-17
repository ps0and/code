import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import io
import sys

def show():
    st.header("1day 파이썬 기초: 자료형, 변수, 리스트")
    st.divider()

    st.subheader("🎥 수업 영상 보기")

    st.subheader("📌 학습 목표")
    st.write("""
    - 파이썬의 기본 자료형과 변수 선언의 이해
    - 리스트 생성과 요소 접근 방법 알기""")
    st.divider()

    st.subheader("ℹ️ 자료형")
    st.write("""          
    - 문자열: 메일 제목, 메시지 내용 등 따옴표('')로 감싸서 입력 Ex. 'Hello World'
    - 숫자열: 물건의 가격, 학생의 성적 Ex. 52, 12
    - 불: 친구의 로그인 상태 Ex. True, False""")

    st.subheader("ℹ️ 출력: print() 함수")
    st.write("""          
    - 함수의 괄호 안에 출력하고 싶은 내용을 적습니다.
    - 함수 뒤에 출력하고 싶은 내용을 쉼표로 연결해서 여러 개 적어도 됩니다.""")
    st.write("""**[문제] 아래와 같이 print 함수를 이용해서 다양한 자료형을 출력해보세요**""")

    # 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    # 레이아웃
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value="print('hello', 320)\nprint(21)",
            language='python',
            theme='dracula',
            height=250,
            key="ace_editor"
        )

    with c2:
        st.markdown("### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기"):
            output_buffer = io.StringIO()
            try:
                sys.stdout = output_buffer
                exec_globals = {}
                exec(code_input, exec_globals)
                sys.stdout = sys.__stdout__
                st.session_state.output = output_buffer.getvalue() or "출력된 내용이 없습니다."
                st.session_state.status = "success"
            except Exception as e:
                sys.stdout = sys.__stdout__
                st.session_state.output = f"{e.__class__.__name__}: {e}"
                st.session_state.status = "error"
                
        # 출력 스타일링
        if st.session_state.status == "success":
            st.markdown(f"```bash\n{st.session_state.output}\n```")
        elif st.session_state.status == "error":
            st.markdown("#### ❌ 실행 중 오류 발생")
            st.markdown(f"<pre style='color: red; background-color: #ffe6e6; padding: 10px; border-radius: 5px;'>{st.session_state.output}</pre>", unsafe_allow_html=True)


        # 사칙연산 정리 데이터
    data = {
        "연산 종류": [
            "덧셈", "뺄셈", "곱셈", "나눗셈", "정수 나눗셈", "나머지", "거듭제곱", "부호 반전"
        ],
        "연산자": ["+", "-", "*", "/", "//", "%", "**", "-"],
        "예시 코드": [
            "3 + 2", "5 - 2", "4 * 2", "10 / 4", "10 // 4", "10 % 4", "2 ** 3", "-7"
        ],
        "결과": [5, 3, 8, 2.5, 2, 2, 8, -7],
        "설명": [
            "두 수를 더함",
            "앞 수에서 뒤 수를 뺌",
            "두 수를 곱함",
            "실수 나눗셈 결과",
            "몫만 구함 (소수점 버림)",
            "나눗셈의 나머지 계산",
            "제곱 (2의 3제곱)",
            "음수 값 표현"
        ]
    }
    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # Streamlit 앱 출력
    st.subheader("🧮 파이썬 사칙연산 정리표")
    st.dataframe(df, use_container_width=True)