import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from streamlit_ace import st_ace
import io, sys, textwrap

# 0) 코드 템플릿 (맨 앞 0열)
RAW_CODE_TEMPLATE = """\
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1) 학생 입력값
seq = [{seq_input}]
n = {term_idx}

# 2) 데이터 전처리
data = np.array(seq, dtype=float)
X, y = [], []
for i in range(len(data) - 1):
    X.append([data[i]])
    y.append(data[i+1])
X = np.array(X).reshape(-1, 1, 1)
y = np.array(y)

# 3) 3층 LSTM 모델 구성
model = Sequential([
    LSTM({units1}, return_sequences=True, input_shape=(1, 1)),
    LSTM({units2}, return_sequences=False),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# 4) 모델 학습
model.fit(X, y, epochs={epochs}, verbose=0)

# 5) 다음 항 예측
last_input = np.array([[[data[-1]]]])
pred = model.predict(last_input)[0, 0]

# 6) 결과 출력
print(f"예측된 {{n}}번째 항: {{pred:.2f}}")
"""

def show():
    st.header("▶️ 수열 예측 인터랙티브 (3층 LSTM)")

    # 1) 하이퍼파라미터 입력
    units1   = st.slider("1층 LSTM 유닛 수",  128, 256, 200, step=10)
    units2   = st.slider("2층 LSTM 유닛 수",  64, 128,  64, step=10)
    epochs   = st.slider("학습 에포크 수",    10, 500, 100, step=10)

    # 2) 수열 입력
    seq_input = st.text_input("콤마로 구분된 수열을 입력하세요", "2,5,8,11")

    # 3) 예측할 항 번호 입력
    term_idx = st.number_input(
        "몇 번째 항을 예측할까요?",
        min_value=1,
        value=len(seq_input.split(",")) + 1,
        step=1
    )

    # 4) full_code 생성 (항상)
    raw_code = RAW_CODE_TEMPLATE.format(
        seq_input=seq_input,
        term_idx=term_idx,
        units1=units1,
        units2=units2,
        epochs=epochs
    )
    full_code = textwrap.dedent(raw_code)

    # 5) 전체 코드 토글
    if "show_full" not in st.session_state:
        st.session_state.show_full = False
    if st.button("코드 생성하기"):
        st.session_state.show_full = True

    # 6) 전체 코드 노출
    if st.session_state.show_full:
        st.subheader("🔍 전체 실행 코드")
        st.code(full_code, language="python")
        if st.checkbox("코드를 바로 실행해보기"):
            buf = io.StringIO()
            try:
                sys.stdout = buf
                exec(full_code, {})
            finally:
                sys.stdout = sys.__stdout__
            st.success(f"실행 결과: {buf.getvalue().strip()}")

        # 7) ACE 에디터 (항상 여기서 렌더링됩니다)
        st.divider()
        st.subheader("📥 실행 코드 (수정 가능)")
        user_code = st_ace(
            value=full_code,         # 항상 표시할 코드
            language="python",
            theme="monokai",
            height=350,
            key="ace_lstm_3layer"
        )
        if st.button("▶️ LSTM 예측 실행하기"):
            buf = io.StringIO()
            try:
                sys.stdout = buf
                exec(user_code, {})
            finally:
                sys.stdout = sys.__stdout__
            st.success(f"실행 결과: {buf.getvalue().strip()}")
