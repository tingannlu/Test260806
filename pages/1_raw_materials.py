import streamlit as st

st.set_page_config(
    page_title="原料｜Raw Materials",
    page_icon="📋",
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
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("← 返回首頁"):
    st.switch_page("streamlit_app.py")

st.markdown(
    """
    <section class="page-header">
        <h1>原料</h1>
        <p>Raw Materials</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="detail-card">
        <strong>01｜Halal 證明文件</strong><br>
        須提供所有投產的原料的 Halal 證。
        無證者以問卷、COA、SDS 等替代。
    </div>

    <div class="detail-card">
        <strong>02｜進口文件</strong><br>
        進口原料須提供進口報單。
    </div>

    <div class="detail-card">
        <strong>03｜資訊一致性</strong><br>
        品名、製造廠、生產地資訊須一致。
    </div>
    """,
    unsafe_allow_html=True,
)
