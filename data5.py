import streamlit as st
from streamlit_ace import st_ace
import io
import sys

# ✅ 코드 실행 함수
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

# ✅ 실행 결과 출력 함수
def display_output(output_key, status_key):
    if st.session_state.get(status_key) == "success":
        st.markdown(f"```bash\n{st.session_state[output_key]}\n```")
    elif st.session_state.get(status_key) == "error":
        st.markdown("##### ❌ 실행 중 오류 발생")
        st.markdown(
            f"<pre style='color: red; background-color: #ffe6e6; padding: 10px; border-radius: 5px;'>"
            f"{st.session_state[output_key]}</pre>",
            unsafe_allow_html=True
        )

# ✅ 좌우 2열 코드 작성 및 실행 블록
def code_block_columns(problem_number, starter_code, prefix=""):
    output_key = f"{prefix}output{problem_number}"
    status_key = f"{prefix}status{problem_number}"
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("##### 📥 코드 입력")
        code_input = st_ace(
            value=starter_code,
            language='python',
            theme='dracula',
            height=220,
            key=f"{prefix}editor{problem_number}"
        )
    with c2:
        st.markdown("##### 📤 실행 결과")
        if st.button("▶️ 코드 실행하기", key=f"{prefix}run{problem_number}"):
            code_runner(code_input, output_key, status_key)
        display_output(output_key, status_key)
    st.divider()

# ✅ 메인 수업 페이지 구성
def show():
    st.header("🗓️ Day 5")
    st.subheader("수열의 합")
    st.write("수열의 각 항을 더한 값을 ‘수열의 합’이라 하고, 대표적으로 등차수열의 합과 등비수열의 합을 파이썬 코드로 직접 구현해 봅시다.")
    st.divider()

    st.subheader("🎥 오늘의 수업 영상")
    st.video("https://youtu.be/wuxmZ8lu79s?si=sdRCeDq5m0blQDv0")

    st.subheader("📌 학습 목표")
    st.write("""
    1. 수열의 합 개념을 이해한다.  
    2. 등차수열의 합을 파이썬을 코드로 구할 수 있다.
    3. 등비수열의 합을 파이썬 코드로 구할 수 있다.
    """)
    st.divider()

    st.subheader("ℹ️ 수열의 합")
    st.write("수열의 항을 순서대로 모두 더한 값을 수열의 합(Series)이라 합니다.")
    st.divider()

    st.subheader("ℹ️ 등차수열의 합 (Arithmetic Series)")
    st.write("- **등차수열의 합**:")
    st.latex(r"S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}\bigl(2a_1 + (n-1)d\bigr)")
    st.write("- 예) $a_1=3$, $d=2$일 때")
    st.latex(r"S_{10} = \frac{10}{2}\bigl(2\times3 + (10-1)\times2\bigr) = 120")


    st.markdown("###### 💻 [예제 1] 첫째 항이 `3`, 공차가 `2`인 등차수열의 첫 `10`항까지 합을 구하는 코드를 작성하세요.")
    code_block_columns(1, "a = 3\nd = 2\nn = 10\n# S_n = n/2 * (2*a + (n-1)*d)\n# 여기에 계산 코드 작성\nprint(S_n)", prefix="d5_")

    st.markdown("##### 💻 [문제 1] 첫째 항이 `2`, 공차가 `5`인 등차수열의 첫 `20`항까지 합을 구하는 코드를 작성하세요.")
    with st.expander("💡 힌트 보기"):
        st.markdown("`S_n = n/2 * (2*a + (n-1)*d)` 공식을 사용하세요.")
    with st.expander("💡 정답 보기"):
        st.code("""
    a = 2
    d = 5
    n = 20
    S_n = n/2 * (2*a + (n-1)*d)
    print(S_n)
    # 출력: 4200
    """)
    code_block_columns(2, "a = 2\nd = 5\nn = 20\n# 여기에 계산 코드 작성\nprint(S_n)", prefix="d5_")

    st.subheader("ℹ️ 등비수열의 합 (Geometric Series)")
    st.write("""
    - 등비수열의 합: 첫째 항 $a_1$, 공비 $r$ ($r\neq1$), $n$항까지의 합 $S_n$는
    $$
    S_n = a_1 \frac{r^n - 1}{r - 1}
    $$
    - 예) $a_1=3$, $r=2$일 때 10항까지의 합은
    $$
    S_{10} = 3\frac{2^{10} -1}{2-1} = 3(1023) = 3069
    $$
    """)

    st.markdown("###### 💻 [예제 2] 첫째 항이 `3`, 공비가 `2`인 등비수열의 첫 `10`항까지 합을 구하는 코드를 작성하세요.")
    code_block_columns(3, "a = 3\nr = 2\nn = 10\n# S_n = a * (r**n - 1) / (r - 1)\n# 여기에 계산 코드 작성\nprint(S_n)", prefix="d5_")

    st.markdown("##### 💻 [문제 2] 첫째 항이 `5`, 공비가 `3`인 등비수열의 첫 `8`항까지 합을 구하는 코드를 작성하세요.")
    with st.expander("💡 힌트 보기"):
        st.markdown("`S_n = a * (r**n - 1) / (r - 1)` 공식을 사용하세요.")
    with st.expander("💡 정답 보기"):
        st.code("""
    a = 5
    r = 3
    n = 8
    S_n = a * (r**n - 1) / (r - 1)
    print(S_n)
    # 출력: 3280
    """)
    code_block_columns(4, "a = 5\nr = 3\nn = 8\n# 여기에 계산 코드 작성\nprint(S_n)", prefix="d5_")

    st.markdown("###### 💻 [도전 문제] 수열의 합 문제 만들기")
    st.write("학생 문제 설명과 작성 코드는 실행 결과 아래에서 확인할 수 있습니다.")

    student_problem = st.text_area(
        "📝 문제 설명 입력",
        value=st.session_state.get("student_problem_text", "초항이 4이고 공비가 3인 등비수열의 첫 `8`항까지의 합을 구하는 코드를 작성하세요.")
    )
    st.session_state["student_problem_text"] = student_problem

    if "custom_code" not in st.session_state:
        st.session_state["custom_code"] = "# 여기에 로직을 작성하세요\n"
    user_code = st_ace(
        value=st.session_state["custom_code"],
        language="python",
        theme="monokai",
        height=250,
        key="ace_custom"
    )
    st.session_state["custom_code"] = user_code

    if st.button("▶️ 실행 결과 확인"):
        code_runner(user_code, "custom_out", "custom_status")
        display_output("custom_out", "custom_status")
        combined = (
            f"# 🔍 학생 문제 설명\n{student_problem}\n\n"
            f"# 💻 학생 작성 코드\n{user_code}"
        )
        st.code(combined)

if __name__ == "__main__":
    show()

