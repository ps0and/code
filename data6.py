import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from streamlit_ace import st_ace
import matplotlib.pyplot as plt
import io, sys, textwrap

def show():
    st.header("▶️ 수열 예측")

    # 1) 모델 선택
    model = st.radio("모델을 선택하세요", ["LinearRegression", "PolynomialRegression"])
    degree = st.slider("다항 회귀 차수 선택", 2, 5, 2) if model=="PolynomialRegression" else None

    # 2) 수열 입력
    seq_input = st.text_input("수열을 입력하세요 (예: 2,5,8,11)", "2,5,8,11")

    # 3) 예측할 항 번호 입력
    term_idx = st.number_input("예측할 항 번호를 입력하세요",
                               min_value=1, value=len(seq_input.split(","))+1)

    # 4) 코드 템플릿 생성
    if model=="LinearRegression":
        raw = f"""
import numpy as np
from sklearn.linear_model import LinearRegression

seq = [{seq_input}]
n = {term_idx}

X = np.arange(1, len(seq)+1).reshape(-1,1)
y = np.array(seq)

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[n]])[0]
"""
    else:
        raw = f"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

seq = [{seq_input}]
n = {term_idx}

X = np.arange(1, len(seq)+1).reshape(-1,1)
y = np.array(seq)

poly = PolynomialFeatures(degree={degree}, include_bias=False)
Xp = poly.fit_transform(X)
model = LinearRegression()
model.fit(Xp, y)

pred = model.predict(poly.transform([[n]]))[0]
"""
    full_code = textwrap.dedent(raw)

    # 5) ACE 에디터: 항상 최신 full_code 반영
    signature = f"{model}|{seq_input}|{term_idx}|{degree}"
    user_code = st_ace(
        value=full_code,
        language="python",
        theme="monokai",
        height=300,
        key=f"ace_{signature}"
    )

    # 6) 실행 및 시각화
    if st.button("▶️ 예측 실행 및 시각화"):
        buf = io.StringIO()
        # exec할 때 로컬 실행 공간을 dict로 만들어 seq, pred, n을 뽑아옵니다.
        exec_locals = {}
        try:
            sys.stdout = buf
            exec(user_code, {}, exec_locals)
        finally:
            sys.stdout = sys.__stdout__

        # 캡처된 프린트 결과
        output = buf.getvalue().strip()
        st.success(f"실행 결과: {output}")

        # 시각화
        seq = exec_locals.get("seq", [])
        pred = exec_locals.get("pred", None)
        n = exec_locals.get("n", None)

        if seq and (pred is not None) and (n is not None):
            fig, ax = plt.subplots()
            ax.plot(range(1, len(seq)+1), seq, marker="o", label="input sequence")
            ax.scatter(n, pred, color="red", label=f"{n}th predicted value")
            ax.set_title("Sequence and prediction results")
            ax.set_xlabel("number")
            ax.set_ylabel("value")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)
        else:
            st.warning("`seq`, `pred`, `n` The value is not properly defined.")

# 실제 앱에서는 아래처럼 show()를 호출합니다.
if __name__ == "__main__":
    show()
