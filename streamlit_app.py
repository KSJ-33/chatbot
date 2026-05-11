import streamlit as st
from openai import OpenAI

# 페이지 설정
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

/* 전체 */
.stApp {
    background: #0f1115;
    color: #f5f5f5;
}

/* 메인 폭 */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* 상단 헤더 */
.hero {
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.05),
            rgba(255,255,255,0.02)
        );
        
    border: 1px solid rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);

    padding: 2.5rem;
    border-radius: 30px;

    margin-bottom: 2rem;
}

/* 타이틀 */
.hero-title {
    font-size: 3.4rem;
    font-weight: 800;
    letter-spacing: -1px;
    color: white;
    margin-bottom: 0.3rem;
}

/* 서브 */
.hero-sub {
    font-size: 1.05rem;
    color: #b4bcd0;
    line-height: 1.7;
}

/* 글래스 카드 */
.glass-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.05);

    padding: 1.2rem;
    border-radius: 22px;

    backdrop-filter: blur(20px);
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: #12151b;
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* 사이드바 글씨 */
section[data-testid="stSidebar"] * {
    color: #e8ecf3;
}

/* 채팅 입력창 */
.stChatInput {
    margin-top: 1rem;
}

.stChatInput input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;

    color: white !important;

    border-radius: 18px !important;

    padding: 1rem !important;
}

/* USER CHAT */
.user-msg {
    background: linear-gradient(
        135deg,
        #5b8cff,
        #7b61ff
    );

    padding: 1rem 1.2rem;
    border-radius: 22px;

    color: white;

    width: fit-content;
    margin-left: auto;

    max-width: 80%;

    box-shadow:
        0 10px 30px rgba(91,140,255,0.25);
}

/* AI CHAT */
.ai-msg {
    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.05);

    padding: 1rem 1.2rem;

    border-radius: 22px;

    color: #f3f5f7;

    max-width: 85%;

    line-height: 1.8;
}

/* 추천 카드 */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;

    margin-top: 1.2rem;
}

.feature-card {
    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.05);

    padding: 1.2rem;

    border-radius: 20px;

    transition: 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-4px);

    background: rgba(255,255,255,0.06);
}

.feature-title {
    font-weight: 700;
    margin-top: 0.5rem;
    margin-bottom: 0.3rem;
}

.feature-desc {
    color: #9ea7bb;
    font-size: 0.92rem;
    line-height: 1.6;
}

/* 모바일 */
@media (max-width: 768px) {

    .hero-title {
        font-size: 2.4rem;
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
        스페셜티 커피 · 브랜딩 · 메뉴 기획 · 감성 카페 컨설팅<br>
        트렌디한 카페 경험을 만드는 AI 바리스타
    </div>

    <div class="feature-grid">

        <div class="feature-card">
            <div style="font-size:1.5rem;">☕</div>
            <div class="feature-title">
                원두 큐레이션
            </div>
            <div class="feature-desc">
                취향 기반 원두 추천과 풍미 분석
            </div>
        </div>

        <div class="feature-card">
            <div style="font-size:1.5rem;">🎨</div>
            <div class="feature-title">
                카페 브랜딩
            </div>
            <div class="feature-desc">
                무드 · 공간 · 로고 · 브랜드 톤 제안
            </div>
        </div>

        <div class="feature-card">
            <div style="font-size:1.5rem;">📈</div>
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
<div class="glass-card">

### Today's Mood

**Colombia Supremo**

Nutty · Chocolate · Smooth

<br>

### 추천 질문

- 요즘 유행하는 카페 인테리어 알려줘
- 시그니처 메뉴 추천해줘
- 인스타 감성 브랜딩 해줘
- 여름 시즌 음료 기획해줘

</div>
""", unsafe_allow_html=True)

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

    # 세션 상태
    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
안녕하세요.
저는 카페 전문 AI 바리스타입니다 ☕

카페 브랜딩, 메뉴 기획,
원두 추천, 공간 컨셉,
SNS 감성 마케팅까지 도와드릴게요.
"""
            }
        ]

    # 기존 메시지
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

    # 입력창
    if prompt := st.chat_input(
        "카페 브랜딩이나 메뉴 아이디어를 물어보세요..."
    ):

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):

            st.markdown(
                f"""
                <div class="user-msg">
                {prompt}
                </div>
                """,
                unsafe_allow_html=True
            )

        # SYSTEM PROMPT
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

        # GPT 호출
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

        # 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
