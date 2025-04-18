import streamlit as st
from streamlit_ace import st_ace
import io
import sys

# ✅ 실행 함수
def code_runner(code_input, output_key, status_key):
    output_buffer = io.StringIO()
    try:
        sys.stdout = output_buffer
        exec_globals = {}
        exec(code_input, exec_globals)
        sys.stdout = sys.__stdout__
        st.session_state[output_key] = output_buffer.getvalue() or "출력된 내용이 없습니다."
        st.session_state[status_key] = "success"
    except Exception as e:
        sys.stdout = sys.__stdout__
        st.session_state[output_key] = f"{e.__class__.__name__}: {e}"
        st.session_state[status_key] = "error"

# ✅ 출력 함수
def display_output(output_key, status_key):
    if st.session_state.get(status_key) == "success":
        st.markdown(f"```bash\n{st.session_state[output_key]}\n```")
    elif st.session_state.get(status_key) == "error":
        st.markdown("#### ❌ 실행 중 오류 발생")
        st.markdown(
            f"<pre style='color: red; background-color: #ffe6e6; padding: 10px; border-radius: 5px;'>{st.session_state[output_key]}</pre>",
            unsafe_allow_html=True
        )

# ✅ 좌우(2열) 코드 블록
def code_block_columns(problem_number, starter_code):
    output_key = f"output{problem_number}"
    status_key = f"status{problem_number}"
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📥 코드 입력")
        code_input = st_ace(
            value=starter_code,
            language='python',
            theme='dracula',
            height=220,
            key=f"editor{problem_number}"
        )
    with c2:
        st.markdown("### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기", key=f"run{problem_number}"):
            code_runner(code_input, output_key, status_key)
        display_output(output_key, status_key)
    st.divider()

# ✅ 상하(1열) 코드 블록
def code_block_rows(problem_number, starter_code):
    output_key = f"output{problem_number}"
    status_key = f"status{problem_number}"
    st.markdown("### 📥 코드 입력")
    code_input = st_ace(
        value=starter_code,
        language='python',
        theme='dracula',
        height=200,
        key=f"editor{problem_number}"
    )
    if st.button("▶️ 코드 실행하기", key=f"run{problem_number}"):
        code_runner(code_input, output_key, sstatus_key)
    st.markdown("### 📤 실행 결과")
    display_output(output_key, status_key)
    st.divider()

# ✅ 메인 수업 내용
def show():
    st.header("🗓️ 3day")
    st.subheader("수열 코딩하기")
    st.write("1day~2day 학습했던 문법을 이용하여 수열을 코딩합시다")
    st.divider()

    st.subheader("🎥 수업 영상 보기")
    st.video("https://youtu.be/wuxmZ8lu79s?si=sdRCeDq5m0blQDv0")

    st.subheader("📌 학습 목표")
    st.write("""
    - 조건문(if/else)의 기본 구조 이해
    - 짝수/홀수 판별 프로그램 만들기
    - 반복문(for)의 구조 이해 및 실습
    """)
    st.divider()

    st.subheader("ℹ️ 조건문 기본")
    st.code("""
    if 조건:
        조건이 True일 때 실행할 코드
    else:
        조건이 False일 때 실행할 코드
    """)
    st.markdown("""##### 💻 [문제 1] 조건문을 사용해 `a > b`인 경우 메시지를 출력해보세요""")
    code_block_rows(1, """a = 10\nb = 3\nif a > b:\n    print('a는 b보다 크다')\nelse:\n    print('a는 b보다 작거나 같다')""")

    st.markdown("""##### 💻 [문제 2]  아래 코드는 짝수/홀수를 정확히 판별하지 못합니다. 조건을 수정하여 `num`이 짝수인지 홀수인지 정확히 출력되도록 코드를 고쳐보세요""")
    code_block_columns(2, """num = 1\nif num :\n    print('num은 짝수')\nelse:\n    print('num은 홀수')""")

    st.subheader("ℹ️ 반복문 for")
    st.write("""
    - 범위 `range(start,end)`는 start부터 end-1까지의 정수로 범위를 만든다.  
    """)
    st.write("""
    - `for`반복문은 특정 작업을 여러 번 반복할 때 사용 
    - 범위에 있는 요소 하나하나가 반복자(변수)에 들어가며 차례차례 아래 코드가 반복된다.
    """)
    st.code("""
    for 반복자 in 반복할 수 있는 것: #반복할 수 있는 것에 리스트, 범위 등이 있다.
        코드
    """)
    st.code("""
    for i in range(1,4): #범위에 있는 요소 1,2,3 하나하나가 i라는 변수에 들어간다.
        print(i) #print()함수로 i를 출력한다.
    # 출력: 1,2,3
    """)

    st.markdown("""##### 💻 [문제 3] 1부터 10까지 숫자를 출력하는 코드를 작성하세요""")
    code_block_columns(3, """for i""")

    st.markdown("""##### 💻 [발전 문제] 1부터 5까지의 합을 구하는 코드를 작성하세요""")
    code_block_columns(4, """total = 0 #초기값 설정\nfor i """)
