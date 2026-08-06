import streamlit as st

st.set_page_config(
    page_title="國光流感疫苗 Halal 認證經驗",
    page_icon="☪️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# Page design
# --------------------------------------------------

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f6f3ea;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        .hero {
            background: linear-gradient(120deg, #123f2c, #287151);
            border-radius: 24px;
            padding: 55px 50px;
            margin-bottom: 48px;
            box-shadow: 0 14px 35px rgba(18, 63, 44, 0.20);
        }

        .hero-label {
            color: #e2c66f;
            font-size: 0.88rem;
            font-weight: 700;
            letter-spacing: 0.15em;
            margin-bottom: 12px;
        }

        .hero h1 {
            color: white !important;
            font-size: 2.7rem;
            line-height: 1.3;
            margin: 0 0 18px 0;
        }

        .hero p {
            color: #edf6f0 !important;
            font-size: 1.08rem;
            line-height: 1.8;
            max-width: 850px;
            margin: 0;
        }

        .section-label {
            color: #9a7727;
            font-size: 0.84rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            margin-bottom: 5px;
        }

        .section-title {
            color: #173d2c;
            font-size: 2rem;
            font-weight: 750;
            margin-bottom: 8px;
        }

        .section-description {
            color: #5c6b62;
            margin-bottom: 25px;
        }

        .card-number {
            color: #a9832e;
            font-size: 0.88rem;
            font-weight: 750;
            letter-spacing: 0.12em;
        }

        .card-title {
            color: #173d2c;
            font-size: 1.5rem;
            font-weight: 750;
            margin-top: 12px;
        }

        .card-subtitle {
            color: #947126;
            font-size: 0.95rem;
            font-weight: 650;
            margin-bottom: 16px;
        }

        .card-copy {
            color: #536158;
            line-height: 1.7;
            min-height: 88px;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: white;
            border-color: #dcd2b9;
            border-radius: 17px;
            box-shadow: 0 7px 22px rgba(23, 61, 44, 0.07);
        }

        .stButton > button {
            background-color: #1d6545;
            color: white;
            border: 1px solid #1d6545;
            border-radius: 10px;
            font-weight: 650;
            min-height: 44px;
        }

        .stButton > button:hover {
            background-color: #154c34;
            color: white;
            border-color: #154c34;
        }

        details {
            background-color: white;
            border: 1px solid #dcd2b9;
            border-radius: 13px;
            padding: 5px 12px;
        }

        @media (max-width: 700px) {
            .hero {
                padding: 35px 25px;
            }

            .hero h1 {
                font-size: 2rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Top introduction
# --------------------------------------------------

st.html(
    """
    <section class="hero">
        <div class="hero-label">
            HALAL CERTIFICATION EXPERIENCE
        </div>

        <h1>
            國光三價及四價流感疫苗<br>
            Halal 認證經驗
        </h1>

        <p>
            分享國光三價及四價流感疫苗進行 Halal 認證時，
            在原料審查、共用生產線，以及清潔與設備管理方面的經驗。
        </p>
    </section>
    """
)
# --------------------------------------------------
# Three core areas
# --------------------------------------------------

st.markdown(
    """
    <div class="section-label">THREE CORE AREAS</div>
    <div class="section-title">Halal 三大核心</div>
    <div class="section-description">
        點選下方按鈕，查看每一項核心內容的詳細說明。
    </div>
    """,
    unsafe_allow_html=True,
)

column_1, column_2, column_3 = st.columns(3, gap="large")

with column_1:
    with st.container(border=True):
        st.markdown(
            """
            <div class="card-number">01</div>
            <div class="card-title">原料</div>
            <div class="card-subtitle">Raw Materials</div>

            <div class="card-copy">
                原料 Halal 證明、替代文件、進口報單，
                以及原料資訊一致性。
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "查看原料詳情 →",
            key="raw_materials",
            use_container_width=True,
        ):
            st.switch_page("pages/1_raw_materials.py")

with column_2:
    with st.container(border=True):
        st.markdown(
            """
            <div class="card-number">02</div>
            <div class="card-title">共用生產線</div>
            <div class="card-subtitle">Shared Production Lines</div>

            <div class="card-copy">
                評估不同產品共用設備、器皿與儲存空間時的
                Halal 風險。
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "查看共線詳情 →",
            key="shared_lines",
            use_container_width=True,
        ):
            st.switch_page("pages/2_shared_production_lines.py")

with column_3:
    with st.container(border=True):
        st.markdown(
            """
            <div class="card-number">03</div>
            <div class="card-title">清潔與設備</div>
            <div class="card-subtitle">Cleaning & Equipment</div>

            <div class="card-copy">
                確認濾膜材質，以及清潔工具與清潔劑符合
                Halal 要求。
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "查看清潔與設備詳情 →",
            key="cleaning_equipment",
            use_container_width=True,
        ):
            st.switch_page("pages/3_cleaning_and_equipment.py")

# --------------------------------------------------
# Milestones
# --------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-label">PROJECT JOURNEY</div>
    <div class="section-title">專案里程碑</div>
    <div class="section-description">
        點選每張里程碑卡片，即可展開閱讀詳細內容。
    </div>
    """,
    unsafe_allow_html=True,
)

left_column, right_column = st.columns(2, gap="large")

with left_column:
    with st.expander("里程碑 1｜專案啟動"):
        st.write(
            """
            請在此處填入：

            - 日期
            - 專案背景
            - 參與單位
            - 主要工作
            """
        )

    with st.expander("里程碑 3｜文件準備與改善"):
        st.write(
            """
            請在此處填入：

            - 文件蒐集
            - 缺口分析
            - 供應商聯繫
            - 改善措施
            """
        )

with right_column:
    with st.expander("里程碑 2｜認證範圍確認"):
        st.write(
            """
            請在此處填入：

            - 認證產品
            - 生產範圍
            - 原料範圍
            - 風險評估
            """
        )

    with st.expander("里程碑 4｜查核與認證完成"):
        st.write(
            """
            請在此處填入：

            - 現場查核
            - 問題回覆
            - 最終確認
            - 認證成果
            """
        )

st.markdown("---")

st.caption(
    "國光三價及四價流感疫苗 Halal 認證經驗｜"
    "Built with Streamlit, GitHub and Render"
)
