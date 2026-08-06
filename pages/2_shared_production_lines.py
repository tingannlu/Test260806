import streamlit as st

st.set_page_config(
    page_title="共用生產線｜Shared Production Lines",
    page_icon="🏭",
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
        <h1>共用生產線</h1>
        <p>Shared Production Lines</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="detail-card">
        <strong>01｜共用生產線定義</strong><br>
        係指任何兩支產品，共用生產設備、器皿或儲存空間。
    </div>

    <div class="detail-card warning-card">
        <strong>02｜Haram 風險</strong><br>
        共線（申請廠、原料廠）產品若含豬成份或其衍生物，
        為 Haram。
    </div>
    """,
    unsafe_allow_html=True,
)
