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
# =========================================================
# MILESTONES — VERTICAL TIMELINE
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.html(
    """
    <style>
        .timeline-section {
            margin-top: 15px;
            margin-bottom: 45px;
        }

        .timeline-label {
            color: #987424;
            font-size: 0.84rem;
            font-weight: 700;
            letter-spacing: 0.15em;
            margin-bottom: 5px;
        }

        .timeline-heading {
            color: #173d2c;
            font-size: 2rem;
            font-weight: 750;
            margin-bottom: 8px;
        }

        .timeline-description {
            color: #5c6b62;
            margin-bottom: 35px;
        }

        .timeline {
            position: relative;
            margin-left: 10px;
            padding-bottom: 10px;
        }

        /* Vertical connecting line */
        .timeline::before {
            content: "";
            position: absolute;
            top: 8px;
            bottom: 8px;
            left: 15px;
            width: 3px;
            background-color: #d6c69f;
            border-radius: 10px;
        }

        .timeline-item {
            position: relative;
            padding-left: 62px;
            margin-bottom: 34px;
        }

        /* Timeline circle */
        .timeline-dot {
            position: absolute;
            top: 7px;
            left: 7px;
            width: 19px;
            height: 19px;
            background-color: #1d6545;
            border: 4px solid #f6f3ea;
            border-radius: 50%;
            box-shadow: 0 0 0 2px #b19043;
            z-index: 2;
        }

        .timeline-number {
            color: #987424;
            font-size: 0.78rem;
            font-weight: 750;
            letter-spacing: 0.12em;
            margin-bottom: 5px;
        }

        /* Override the previous expander/card appearance */
        .timeline details {
            background: transparent !important;
            border: none !important;
            border-radius: 0 !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        .timeline summary {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            cursor: pointer;
            list-style: none;
            padding: 0 0 10px 0;
            border-bottom: 1px solid #d8cfb8;
        }

        .timeline summary::-webkit-details-marker {
            display: none;
        }

        .timeline-title {
            color: #173d2c;
            font-size: 1.3rem;
            font-weight: 750;
        }

        .timeline-toggle {
            color: #1d6545;
            font-size: 0.85rem;
            font-weight: 700;
            white-space: nowrap;
        }

        .timeline-toggle::after {
            content: " ＋";
            font-size: 1.1rem;
        }

        .timeline details[open] .timeline-toggle::after {
            content: " －";
        }

        .timeline-content {
            color: #46564d;
            line-height: 1.8;
            padding: 18px 0 4px 0;
        }

        .timeline-content p {
            color: #46564d;
            margin-top: 0;
        }

        .timeline-content ul {
            margin-top: 8px;
            padding-left: 22px;
        }

        .timeline-content li {
            color: #46564d;
            margin-bottom: 6px;
        }

        @media (max-width: 700px) {
            .timeline-item {
                padding-left: 48px;
            }

            .timeline-title {
                font-size: 1.08rem;
            }

            .timeline summary {
                align-items: flex-start;
            }

            .timeline-toggle {
                font-size: 0;
            }

            .timeline-toggle::after {
                font-size: 1.2rem;
            }
        }
    </style>

    <section class="timeline-section">

        <div class="timeline-label">
            PROJECT JOURNEY
        </div>

        <div class="timeline-heading">
            專案里程碑
        </div>

        <div class="timeline-description">
            依時間順序呈現專案進程。點選每一項即可展開詳細內容。
        </div>

        <div class="timeline">

            <div class="timeline-item">
                <div class="timeline-dot"></div>

                <div class="timeline-number">
                    MILESTONE 01
                </div>

                <details>
                    <summary>
                        <span class="timeline-title">
                            專案啟動
                        </span>

                        <span class="timeline-toggle">
                            點選展開
                        </span>
                    </summary>

                    <div class="timeline-content">
                        <p><strong>日期：</strong>請填入日期</p>

                        <ul>
                            <li>專案背景與認證需求確認</li>
                            <li>成立跨部門專案團隊</li>
                            <li>確認參與單位及負責人</li>
                            <li>規劃專案時程及主要工作</li>
                        </ul>
                    </div>
                </details>
            </div>


            <div class="timeline-item">
                <div class="timeline-dot"></div>

                <div class="timeline-number">
                    MILESTONE 02
                </div>

                <details>
                    <summary>
                        <span class="timeline-title">
                            認證範圍確認
                        </span>

                        <span class="timeline-toggle">
                            點選展開
                        </span>
                    </summary>

                    <div class="timeline-content">
                        <p><strong>日期：</strong>請填入日期</p>

                        <ul>
                            <li>確認三價及四價流感疫苗認證範圍</li>
                            <li>確認原料及供應商範圍</li>
                            <li>確認生產線、設備及儲存空間</li>
                            <li>進行初步 Halal 風險評估</li>
                        </ul>
                    </div>
                </details>
            </div>


            <div class="timeline-item">
                <div class="timeline-dot"></div>

                <div class="timeline-number">
                    MILESTONE 03
                </div>

                <details>
                    <summary>
                        <span class="timeline-title">
                            文件準備與改善
                        </span>

                        <span class="timeline-toggle">
                            點選展開
                        </span>
                    </summary>

                    <div class="timeline-content">
                        <p><strong>日期：</strong>請填入日期</p>

                        <ul>
                            <li>蒐集原料 Halal 證、COA、SDS 及問卷</li>
                            <li>確認進口原料報單</li>
                            <li>核對品名、製造廠及生產地資訊</li>
                            <li>完成缺口分析及改善措施</li>
                        </ul>
                    </div>
                </details>
            </div>


            <div class="timeline-item">
                <div class="timeline-dot"></div>

                <div class="timeline-number">
                    MILESTONE 04
                </div>

                <details>
                    <summary>
                        <span class="timeline-title">
                            查核與認證完成
                        </span>

                        <span class="timeline-toggle">
                            點選展開
                        </span>
                    </summary>

                    <div class="timeline-content">
                        <p><strong>日期：</strong>請填入日期</p>

                        <ul>
                            <li>接受文件審查及現場查核</li>
                            <li>回覆查核問題</li>
                            <li>完成改善事項確認</li>
                            <li>取得 Halal 認證</li>
                        </ul>
                    </div>
                </details>
            </div>

        </div>
    </section>
    """
)
# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        國光三價及四價流感疫苗 Halal 認證經驗
        <br>
        Built with Streamlit, GitHub and Render
    </div>
    """,
    unsafe_allow_html=True,
)
