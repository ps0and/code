import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import io
import sys

def show():
    if "status" not in st.session_state:
        st.session_state.status = ""
    if "output" not in st.session_state:
        st.session_state.output = ""
    st.header("🗓️2day")
    st.subheader("파이썬 기초: 조건문, 반복문")
    st.write("수학을 코딩하기위해서는 코딩에 대한 기본 문법을 알고 있어야 합니다.")
    st.write("코딩 시작합니다.")
    st.divider()

    st.subheader("🎥 수업 영상 보기")
    st.video("https://youtu.be/wuxmZ8lu79s?si=sdRCeDq5m0blQDv0")
    st.subheader("📌 학습 목표")
    st.write("""
    - 파이썬의 기본 자료형과 변수 선언의 이해
    - 리스트 생성과 요소 접근 방법 알기""")
    st.divider()

    st.subheader("ℹ️ 조건문")
    st.write("""
    - 조건에 따라 코드를 실행하거나, 실행하지 않게 만들고 싶을 때 사용하는 구문
    - ```if```: 주어진 조건이 참(True)일 때 특정 코드를 실행합니다.
    - ```else```: 모든 조건이 거짓일 때 실행되는 코드를 정의합니다.        
    - ```if 조건:``` 조건을 입력하고 반드지 ```:```를 입력한다. 
    """) 
    st.code("""
    if 조건:
        조건이 True인 경우 실행될 명령어
    else:
        조건이 False인 경우 실행될 명령어
    """) 
    st.subheader("🧮 파이썬 사칙연산 정리표")
    st.image("image\data2_img1.png")

    st.markdown("""##### 💻[문제] 아래와 같이 조건문을 이용하여 참인 결과를 출력해보세요""")

    # 세션 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    st.markdown("### 📥 코드 입력")
    code_input = st_ace(
        value="a = 10\nb = 3\nif a > b:#a가b보다 크다면\n    print('a는 b보다 크다')#조건이 참인경우 a가b보다 크다 출력\nelse:\n    print('a는 b보다 작거나 같습니다')#거짓인 경우 a가b보다 작거나 같다 출력",
        language='python',
        theme='dracula',
        height=200,
        key="ace_editor1"
    )

    # 실행 버튼
    if st.button("▶️ 코드 실행하기", key="run1"):
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

    # 실행 결과 표시
    st.markdown("### 📤 실행 결과")
    if st.session_state.status == "success":
        st.markdown(f"```bash\n{st.session_state.output}\n```")
    elif st.session_state.status == "error":
        st.markdown("#### ❌ 실행 중 오류 발생")
        st.markdown(
            f"<pre style='color: red; background-color: #ffe6e6; padding: 10px; border-radius: 5px;'>{st.session_state.output}</pre>",
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown("""##### 💻[발전문제] 조건문을 이용하여 num에 입력된 값이 짝수인지 홀수인지 구분하는 프로그램을 작성하세요""")
     # 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    # 레이아웃
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value="num = \nif :\n    print('num은 짝수입니다')\nelse:\n    print('num은 홀수입니다.')",
            language='python',
            theme='dracula',
            height=250,
            key="ace_editor2"
        )

    with c2:
        st.markdown("### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기",key="run2"):
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
    st.divider()

    st.subheader("ℹ️ 반복문")
    st.write("""
    - 조건에 따라 코드를 실행하거나, 실행하지 않게 만들고 싶을 때 사용하는 구문
    - ```if```: 주어진 조건이 참(True)일 때 특정 코드를 실행합니다.
    - ```else```: 모든 조건이 거짓일 때 실행되는 코드를 정의합니다.        
    - ```if 조건:``` 조건을 입력하고 반드지 ```:```를 입력한다. 
    """) 
    st.code("""
    if 조건:
        조건이 True인 경우 실행될 명령어
    else:
        조건이 False인 경우 실행될 명령어
    """) 

    st.markdown("""##### 💻[문제] 아래와 같이 조건문을 이용하여 참인 결과를 출력해보세요""")

    # 세션 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    st.markdown("### 📥 코드 입력")
    code_input = st_ace(
        value="a = 10\nb = 3\nif a > b:#a가b보다 크다면\n    print('a는 b보다 크다')#조건이 참인경우 a가b보다 크다 출력\nelse:\n    print('a는 b보다 작거나 같습니다')#거짓인 경우 a가b보다 작거나 같다 출력",
        language='python',
        theme='dracula',
        height=200,
        key="ace_editor3"
    )

    # 실행 버튼
    if st.button("▶️ 코드 실행하기", key="run3"):
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

    # 실행 결과 표시
    st.markdown("### 📤 실행 결과")
    if st.session_state.status == "success":
        st.markdown(f"```bash\n{st.session_state.output}\n```")
    elif st.session_state.status == "error":
        st.markdown("#### ❌ 실행 중 오류 발생")
        st.markdown(
            f"<pre style='color: red; background-color: #ffe6e6; padding: 10px; border-radius: 5px;'>{st.session_state.output}</pre>",
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown("""##### 💻[발전문제] 조건문을 이용하여 num에 입력된 값이 짝수인지 홀수인지 구분하는 프로그램을 작성하세요""")
     # 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    # 레이아웃
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value="num = \nif :\n    print('num은 짝수입니다')\nelse:\n    print('num은 홀수입니다.')",
            language='python',
            theme='dracula',
            height=250,
            key="ace_editor4"
        )

    with c2:
        st.markdown("### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기",key="run4"):
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
    st.divider()