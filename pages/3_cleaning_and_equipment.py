import streamlit as st

st.set_page_config(
    page_title="清潔與設備｜Cleaning & Equipment",
    page_icon="🧼",
    layout="wide",
)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f6f3ea;
        }

        .block-container {
            max-width: 950px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        .page-header {
            background: linear-gradient(120deg, #123f2c, #287151);
            padding: 42px;
            border-radius: 22px;
            margin: 20px 0 35px 0;
        }

        .page-header h1 {
            color: white !important;
            margin: 0;
        }

        .page-header p {
            color: #edf6f0 !important;
            font-size: 1.1rem;
            margin: 8px 0 0 0;
        }

        .detail-card {
            background-color: white;
            border: 1px solid #dcd2b9;
            border-left: 6px solid #ad8730;
            border-radius: 14px;
            padding: 24px 28px;
            margin-bottom: 18px;
            color: #173d2c;
            font-size: 1.08rem;
            line-height: 1.8;
            box-shadow: 0 7px 20px rgba(23, 61, 44, 0.06);
        }

        .warning-card {
            border-left-color: #9e3c34;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("← 返回首頁"):
    st.switch_page("streamlit_app.py")

st.markdown(
    """
    <section class="page-header">
        <h1>清潔與設備</h1>
        <p>Cleaning & Equipment</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="detail-card">
        <strong>01｜濾膜材質</strong><br>
        須提供濾膜材質資訊。
    </div>

    <div class="detail-card warning-card">
        <strong>02｜清潔工具及清潔劑</strong><br>
        不可使用豬鬃刷子、含酯類清潔劑。
    </div>
    """,
    unsafe_allow_html=True,
)
