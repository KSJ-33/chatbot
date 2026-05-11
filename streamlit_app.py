import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(
    page_title="Cafe AI Barista",
    page_icon="☕",
    layout="wide"
)

# 커스텀 CSS
st.markdown("""
<style>

/* 전체 배경 */
.stApp {
    background: linear-gradient(
        135deg,
        #1a120b 0%,
        #3c2a21 50%,
        #d5cea3 100%
    );
    color: white;
}

/* 메인 컨테이너 */
.main-container {
    background: rgba(255,255,255,0.08);
    padding: 2rem;
    border-radius: 24px;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-top: 20px;
}

/* 타이틀 */
.title {
    font-size: 3rem;
    font-weight: 800;
    color: #fff8ea;
    margin-bottom: 0;
}

.subtitle {
    color: #f5ebe0;
    font-size: 1.1rem;
    margin-top: 0.3rem;
    opacity: 0.8;
}

/* 카드 */
.info-card {
    background: rgba(255,255,255,0.08);
    padding: 1rem;
    border-radius: 18px;
    margin-top: 1rem;
    border: 1px solid rgba(255,255,255,0.08);
}

/* 채팅 입력창 */
.stChatInput input {
    background-color: rgba(255,255,255,0.12) !important;
    color: white !important;
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}

/* 사용자 채팅 */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 10px;
    margin-bottom: 10px;
}

/* AI 채팅 */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background: rgba(111, 78, 55, 0.35);
    border-radius: 20px;
    padding: 10px;
    margin-bottom: 10px;
}

/* 버튼 */
.stButton button {
    background: linear-gradient(135deg, #a47148, #6f4e37);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: rgba(20,20,20,0.6);
    border-right: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("""
<div class="main-container">
    <div class="title">☕ Cafe AI Barista</div>
    <div class="subtitle">
        원두 추천부터 카페 브랜딩, 메뉴 개발까지 도와주는 AI 바리스타
    </div>
</div>
""", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown("## ☕ Cafe Assistant")
    
    st.markdown("""
    ### 추천 기능
    - 원두 추천
    - 카페 메뉴 기획
    - 디저트 페어링
    - 카페 브랜딩
    - 인테리어 컨셉
    - SNS 마케팅
    
    ---
    
    ### 오늘의 추천
    **에티오피아 예가체프**
    
    Floral / Citrus / Tea-like
    """)

# API 키 입력
openai_api_key = st.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="sk-..."
)

if not openai_api_key:
    st.info("OpenAI API 키를 입력해주세요 ☕")
else:

    client = OpenAI(api_key=openai_api_key)

    # 세션 상태
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
안녕하세요 ☕  
저는 카페 전문 AI 바리스타입니다.

원두 추천, 메뉴 구성, 카페 창업, 브랜딩,
디저트 페어링 등 무엇이든 물어보세요!
"""
            }
        ]

    # 채팅 출력
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):

            if message["role"] == "assistant":
                st.markdown(f"""
                <div style="
                    background: rgba(111,78,55,0.25);
                    padding: 18px;
                    border-radius: 18px;
                    color: white;
                    line-height: 1.7;
                ">
                {message["content"]}
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.08);
                    padding: 18px;
                    border-radius: 18px;
                    color: white;
                    line-height: 1.7;
                ">
                {message["content"]}
                </div>
                """, unsafe_allow_html=True)

    # 입력창
    if prompt := st.chat_input("카페에 대해 무엇이든 물어보세요 ☕"):

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        # 시스템 프롬프트
        system_prompt = """
당신은 전문 바리스타이자 카페 컨설턴트 AI입니다.

다음 분야에 전문성을 가지고 있습니다:
- 스페셜티 커피
- 원두 추천
- 카페 브랜딩
- 메뉴 기획
- 디저트 페어링
- 카페 창업
- 인테리어 컨셉
- SNS 마케팅

답변은 감성적이고 세련된 톤으로 작성하세요.
"""

        # API 호출
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
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
