import streamlit as st
from openai import OpenAI

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Cafe AI",
    page_icon="☕",
    layout="wide"
)

# =========================
# MODERN UI STYLE
# =========================
st.markdown("""
<style>

/* 전체 배경 */
.stApp {
    background: #0B0F19;
    color: #F5F7FA;
}

/* 메인 레이아웃 */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* 헤더 */
.hero {
    background: #121826;

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 30px;

    padding: 2.8rem;

    margin-bottom: 2rem;
}

/* 타이틀 */
.hero-title {
    font-size: 3.6rem;

    font-weight: 800;

    letter-spacing: -2px;

    color: white;

    margin-bottom: 0.4rem;
}

/* 설명 */
.hero-sub {
    color: #9AA4B2;

    font-size: 1.05rem;

    line-height: 1.8;
}

/* 카드 영역 */
.feature-grid {
    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 1rem;

    margin-top: 2rem;
}

/* 카드 */
.feature-card {
    background: #151C2C;

    border: 1px solid rgba(255,255,255,0.05);

    border-radius: 22px;

    padding: 1.3rem;

    transition: 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-4px);

    border-color: rgba(124,92,255,0.35);
}

/* 카드 제목 */
.feature-title {
    font-size: 1rem;

    font-weight: 700;

    margin-top: 0.8rem;

    margin-bottom: 0.4rem;
}

/* 카드 설명 */
.feature-desc {
    color: #94A3B8;

    line-height: 1.7;

    font-size: 0.93rem;
}

/* 채팅 입력창 */
.stChatInput input {
    background: #151C2C !important;

    color: white !important;

    border: 1px solid rgba(255,255,255,0.06) !important;

    border-radius: 18px !important;

    padding: 1rem !important;
}

/* USER CHAT */
.user-msg {
    background: linear-gradient(
        135deg,
        #7C5CFF,
        #5B8CFF
    );

    color: white;

    padding: 1rem 1.2rem;

    border-radius: 20px;

    width: fit-content;

    margin-left: auto;

    max-width: 80%;
}

/* AI CHAT */
.ai-msg {
    background: #151C2C;

    border: 1px solid rgba(255,255,255,0.04);

    color: #F5F7FA;

    padding: 1rem 1.2rem;

    border-radius: 20px;

    max-width: 85%;

    line-height: 1.8;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: #0F1725;

    border-right: 1px solid rgba(255,255,255,0.05);
}

section[data-testid="stSidebar"] * {
    color: #E6EDF7;
}

/* 모바일 */
@media (max-width: 768px) {

    .hero-title {
        font-size: 2.5rem;
    }

    .feature-grid {
        grid-template-columns: 1fr;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="hero">

    <div class="hero-title">
        Cafe AI
    </div>

    <div class="hero-sub">
        스페셜티 커피 · 카페 브랜딩 · 메뉴 기획 · 감성 마케팅<br>
        트렌디한 카페 경험을 만드는 AI 바리스타
    </div>

    <div class="feature-grid">

        <div class="feature-card">
            <div style="font-size:1.6rem;">☕</div>

            <div class="feature-title">
                원두 큐레이션
            </div>

            <div class="feature-desc">
                취향 기반 원두 추천과 향미 분석
            </div>
        </div>

        <div class="feature-card">
            <div style="font-size:1.6rem;">🎨</div>

            <div class="feature-title">
                카페 브랜딩
            </div>

            <div class="feature-desc">
                로고 · 무드 · 공간 컨셉 제안
            </div>
        </div>

        <div class="feature-card">
            <div style="font-size:1.6rem;">📈</div>

            <div class="feature-title">
                SNS 마케팅
            </div>

            <div class="feature-desc">
                인스타 감성 콘텐츠와 릴스 아이디어
            </div>
        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.markdown("## ☕ Dashboard")

    st.markdown("""
    ### Today's Coffee

    **Ethiopia Yirgacheffe**

    Floral · Citrus · Tea-like

    ---

    ### 추천 질문

    - 요즘 유행하는 카페 인테리어 알려줘
    - 시그니처 메뉴 추천해줘
    - 인스타 감성 브랜딩 해줘
    - 여름 시즌 음료 기획해줘
    """)

# =========================
# API KEY
# =========================
openai_api_key = st.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="sk-..."
)

if not openai_api_key:

    st.info("OpenAI API Key를 입력해주세요 ☕")

else:

    client = OpenAI(api_key=openai_api_key)

    # =========================
    # SESSION STATE
    # =========================
    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
안녕하세요 ☕

저는 카페 전문 AI 바리스타입니다.

원두 추천, 카페 브랜딩,
메뉴 개발, 공간 컨셉,
SNS 마케팅까지 도와드릴게요.
"""
            }
        ]

    # =========================
    # MESSAGE RENDER
    # =========================
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            if message["role"] == "assistant":

                st.markdown(
                    f"""
                    <div class="ai-msg">
                    {message["content"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="user-msg">
                    {message["content"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # =========================
    # CHAT INPUT
    # =========================
    if prompt := st.chat_input(
        "카페 브랜딩이나 메뉴 아이디어를 물어보세요..."
    ):

        # 유저 메시지 저장
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        # 유저 메시지 출력
        with st.chat_message("user"):

            st.markdown(
                f"""
                <div class="user-msg">
                {prompt}
                </div>
                """,
                unsafe_allow_html=True
            )

        # 시스템 프롬프트
        system_prompt = """
당신은 프리미엄 카페 브랜드 전문 AI입니다.

현대적이고 감각적인 톤으로 답변하세요.

전문 분야:
- 카페 브랜딩
- 스페셜티 커피
- 메뉴 개발
- 인테리어 무드
- SNS 마케팅
- 공간 디자인
"""

        # GPT 응답 생성
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },

                *[
                    {
                        "role": m["role"],
                        "content": m["content"]
                    }
                    for m in st.session_state.messages
                ]
            ],

            stream=True,
        )

        # 응답 출력
        with st.chat_message("assistant"):

            response = st.write_stream(stream)

        # 응답 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
