
import streamlit as st
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
    st.subheader("✏️ 1단계: 나만의 등차수열 코드 작성")

    default_code = """# 첫째항이 2이고 공차가 3인 등차수열 앞 5개 항 출력
sequence = []
for i in range(5):
    sequence.append(2 + 3*i)
st.write("등차수열:", sequence)
"""

    user_code = st.text_area("등차수열을 출력하는 코드를 작성해보세요!", height=220, value=default_code)

    # 코드 실행 및 결과 저장
    local_vars = {}

    if st.button("✅ 코드 실행하기"):
        try:
            exec(user_code, {"st": st}, local_vars)
            if "sequence" in local_vars:
                st.success("✅ 코드 실행 완료!")
                st.write("🔍 출력된 수열:", local_vars["sequence"])
            else:
                st.warning("⚠️ 'sequence' 리스트가 정의되지 않았어요. 변수명을 확인해주세요.")
        except Exception as e:
            st.error(f"❌ 오류가 발생했어요: {e}")

    # 채점 기능
    if "sequence" in local_vars:
        st.divider()
        st.subheader("📋 2단계: 자동 채점 결과")

        expected = [2, 5, 8, 11, 14]
        user_seq = local_vars["sequence"]

        if user_seq == expected:
            st.success("🎉 정답입니다! 등차수열을 정확히 출력했어요.")
        else:
            st.error(f"❌ 수열이 정답과 다릅니다.\n\n👉 정답: {expected}\n🧪 당신의 출력: {user_seq}")

        # 시각화
        st.divider()
        st.subheader("📊 3단계: 수열 시각화")

        fig, ax = plt.subplots()
        ax.plot(range(1, len(user_seq)+1), user_seq, marker='o')
        ax.set_title("등차수열 시각화")
        ax.set_xlabel("항 번호")
        ax.set_ylabel("값")
        st.pyplot(fig)
