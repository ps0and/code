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
    st.header("🗓️1day")
    st.subheader("파이썬 기초: 자료형, 변수, 리스트")
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

    st.subheader("ℹ️ 자료형")
    st.write("""          
    - 문자열: 메일 제목, 메시지 내용 등 따옴표('')로 감싸서 입력 Ex.```'Hello World'```
    - 숫자열: 물건의 가격, 학생의 성적 Ex. ```52, 12```
    - 불: 친구의 로그인 상태 Ex. ```True, False```""")
    st.divider()

    st.subheader("ℹ️ 출력: print() 함수")
    st.write("""          
    - ```print()``` 함수의 괄호 안에 출력하고 싶은 내용을 적습니다.
    - ```print(1,'a')``` 함수의 괄호 안에 출력하고 싶은 내용을 쉼표로 연결해서 여러 개 적어도 됩니다.""")
   
    st.markdown("""##### 💻[문제] 아래와 같이 print 함수를 이용해서 다양한 자료형을 출력해보세요""")

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
            key="ace_editor1"
        )

    with c2:
        st.markdown("### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기",key="run1"):
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

        # 사칙연산 정리 데이터
    data = {
        "연산 종류": [
            "덧셈", "뺄셈", "곱셈", "나눗셈", "정수 나눗셈", "나머지", "거듭제곱"
        ],
        "연산자": ["+", "-", "*", "/", "//", "%", "**"],
        "예시 코드": [
            "3 + 2", "5 - 2", "4 * 2", "10 / 4", "10 // 4", "10 % 4", "2 ** 3"
        ],
        "결과": [5, 3, 8, 2.5, 2, 2, 8],
        "설명": [
            "두 수를 더함",
            "앞 수에서 뒤 수를 뺌",
            "두 수를 곱함",
            "실수 나눗셈 결과",
            "몫만 구함 (소수점 버림)",
            "나눗셈의 나머지 계산",
            "제곱 (2의 3제곱)"
        ]
    }
    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # Streamlit 앱 출력
    st.subheader("🧮 파이썬 사칙연산 정리표")
    st.dataframe(df, use_container_width=True)

    st.markdown("""##### 💻[문제] 아래와 같이 숫자의 연산을 출력해보세요""")
     # 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    # 레이아웃
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value="print('5+7=', 5+7)\nprint('5**2=', 5**2)",
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

    st.subheader("ℹ️ 변수와 입력")
    st.write("""          
             - 변수는 값을 저장할 때 사용하는 식별자
             - ```변수 = 값``` (값을 변수에 할당합니다.)
             - ```=``` 기호는 '같다'의 의미가 아니라 우변의 값을 좌변에 '할당하겠다'의 의미""")
   
    st.markdown("""##### 💻[문제] 아래와 같이 x라는 변수에 숫자나 문자를 할당하고 변수를 출력해보세요""")

    # 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    # 레이아웃
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value="pi=3.14\nprint(pi)",
            language='python',
            theme='dracula',
            height=250,
            key="ace_editor3"
        )

    with c2:
        st.markdown("### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기",key="run3"):
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

    st.subheader("ℹ️ 리스트(list) 및 인덱스(index)")
    st.write("""          
    - 리스트란 숫자나 문자 등의 자료를 모아서 사용할 수 있게 해주는 특별한 자료
        - 리스트는 대괄호 [ ] 내부에 여러 종류의 자료를 넣어 선언합니다.
        - [요소, 요소, ..., 요소]
        """)
    st.code("""
    list=[12,'문자열',True]
    print[list]            
    >>> [12,'문자열',True]""")
    st.write("""          
    - 현실은 숫자를 1부터 세지만, 파이썬은 0부터 셉니다. 따라서 각 요소가 들어있는 위치는 아래와 같으며 이를 인덱스라고 합니다. ```list[]```는 인덱스를 추출하며 대괄호 안에 인덱스를 입력합니다.""")
    st.image("image\data1_img1.png")

    st.code("""
    list=[12,'문자열',True]
    print(list[0]) #리스트 기호인 대괄호 안에 들어간 숫자를 인덱스(index)           
    >>> 12""") 
    st.write("""          
    - append 함수는 list에 특정한 자료를 추가합니다. ```list.append()``` 소괄호 안에 특정한 자료를 입력하면 리스트의 마지막 요소에 추가됩니다.
    """)
    st.code("""
    list=['a','b','c']
    list.append('d')      
    print(list)
    >>> [a,b,c,d]""") 

    st.markdown("""##### 💻[문제] 아래와 같이 리스트를 선언하고 자료를 추가합니다. 리스트의 특정 요소를 출력해보세오.""")

    # 상태 초기화
    if "output" not in st.session_state:
        st.session_state.output = ""

    # 레이아웃
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value="list=['a','b','c']\nlist.append('d')\nprint(list[3])",
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