import streamlit as st
from streamlit_ace import st_ace
import matplotlib.pyplot as plt

def show():
    st.subheader("📘 2일차 1교시 수업: 등차수열의 개념")
    st.markdown("""
    - **주제**: 등차수열의 일반항과 합
    - **목표**: 등차수열의 규칙을 이해하고 일반항과 합을 구할 수 있다.
    - **예제**: 2, 5, 8, 11, ... 의 일반항과 합 구하기
    - **활동**: 코드 작성 → 실행 → 채점 → 시각화
    """)

    st.divider()
    st.subheader("✏️ 1단계: 등차수열 만드는 코드 작성")

    default_code = """# 'sequence'라는 리스트에 등차수열을 담아주세요
# 첫째항 2, 공차 3, 항의 개수 5
sequence = []
for i in range(5):
    sequence.append(2 + 3 * i)
"""

    user_code = st_ace(
        placeholder="여기에 파이썬 코드를 입력하세요",
        language="python",
        theme="monokai",
        value=default_code,
        height=220,
        font_size=16,
        key="ace_editor"
    )

    local_vars = {}

    if st.button("✅ 코드 실행하기"):
        try:
            # 제한된 실행 환경 구성 (보안상 안전하게)
            exec(user_code, {"st": st}, local_vars)

            if "sequence" in local_vars:
                user_seq = local_vars["sequence"]
                st.success("✅ 코드 실행 완료!")
                st.write("🔍 생성된 수열:", user_seq)

                # 채점
                st.divider()
                st.subheader("📋 2단계: 자동 채점 결과")

                expected = [2, 5, 8, 11, 14]
                if user_seq == expected:
                    st.success("🎉 정답입니다! 등차수열을 정확히 출력했어요.")
                else:
                    st.error("❌ 수열이 정답과 다릅니다.")
                    st.info(f"👉 정답: {expected}\n🧪 당신의 출력: {user_seq}")

                # 시각화
                st.divider()
                st.subheader("📊 3단계: 수열 시각화")
                fig, ax = plt.subplots()
                ax.plot(range(1, len(user_seq) + 1), user_seq, marker='o')
                ax.set_title("등차수열 시각화")
                ax.set_xlabel("항 번호")
                ax.set_ylabel("값")
                st.pyplot(fig)

            else:
                st.warning("⚠️ 'sequence' 리스트가 정의되지 않았어요. 변수명을 꼭 'sequence'로 해주세요.")

        except Exception as e:
            st.error(f"❌ 코드 실행 중 오류 발생: {e}")
