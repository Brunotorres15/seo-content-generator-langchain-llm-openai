import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* Fundo escuro com padrão de pontos */
    .stApp {
        background-color: #0a0e17;
        background-image: radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.1) 1px, transparent 0);
        background-size: 20px 20px;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Container principal */
    .main {
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem;
    }

    /* Título com efeito neon */
    .header {
        text-align: center;
        margin-bottom: 2.5rem;
    }

    .header h1 {
        font-size: 2.8rem;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin-bottom: 0.5rem;
        position: relative;
        display: inline-block;
    }

    .header h1:after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        border-radius: 2px;
    }

    .header p {
        color: #a0a8c0;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto;
    }

    /* Card estilo futurista */
    .card {
        background: rgba(16, 22, 41, 0.8);
        border: 1px solid rgba(0, 210, 255, 0.2);
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(8px);
        margin-bottom: 2rem;
        transition: all 0.3s ease;
    }

    .card:hover {
        border-color: rgba(0, 210, 255, 0.4);
        box-shadow: 0 8px 40px rgba(0, 210, 255, 0.2);
    }

    /* Inputs modernos */
    .stTextInput>div>div>input, 
    .stTextArea>div>textarea,
    .stSelectbox>div>select {
        background-color: rgba(10, 14, 23, 0.8) !important;
        color: white !important;
        border: 1px solid rgba(0, 210, 255, 0.3) !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput>div>div>input:focus, 
    .stTextArea>div>textarea:focus,
    .stSelectbox>div>select:focus {
        border-color: #00d2ff !important;
        box-shadow: 0 0 0 2px rgba(0, 210, 255, 0.2) !important;
        outline: none !important;
    }

    /* Placeholder */
    ::placeholder {
        color: rgba(160, 168, 192, 0.7) !important;
    }

    /* Botão principal */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: #0a0e17 !important;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 1.5rem;
        transition: all 0.3s ease;
        width: 100%;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 210, 255, 0.4);
    }

    /* Checkbox estilizado */
    .stCheckbox>label {
        color: #a0a8c0 !important;
        font-size: 0.95rem;
    }

    /* Resultado */
    .result-container {
        background: rgba(16, 22, 41, 0.9);
        border: 1px solid rgba(0, 210, 255, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
        position: relative;
    }

    .result-container:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        border-radius: 12px 12px 0 0;
    }

    .result-title {
        color: #00d2ff;
        font-size: 1.2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Efeito de loading */
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }

    .loading-pulse {
        animation: pulse 1.5s infinite;
    }

    /* Responsividade */
    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        
        .header h1 {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
    <div class="main">
        <div class="header">
            <h1>🧠 NeuroContent AI</h1>
            <p>Inteligência artificial especializada em criação de conteúdo otimizado para SEO e conversão</p>
        </div>
    """, unsafe_allow_html=True)

def render_form():
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        
        with st.form("content_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                topic = st.text_input(
                    "**Tema Principal**",
                    placeholder="Ex: saúde mental no ambiente corporativo",
                    help="O assunto central do seu conteúdo"
                )
                
                platform = st.selectbox(
                    "**Plataforma de Publicação**",
                    ["Blog", "LinkedIn", "Instagram", "Facebook", "Site Institucional", "E-mail Marketing"],
                    index=0
                )
                
                tone = st.selectbox(
                    "**Tom de Voz**",
                    ["Profissional", "Informativo", "Inspiracional", "Conversacional", "Autoritário", "Empático"],
                    index=0
                )
                
            with col2:
                length = st.selectbox(
                    "**Extensão do Texto**",
                    ["Curto (150-300 palavras)", "Médio (300-600 palavras)", "Longo (600+ palavras)"],
                    index=1
                )
                
                audience = st.selectbox(
                    "**Público-Alvo**",
                    ["Público-Geral", "Executivos", "Profissionais de TI", "Empreendedores", "Jovens Adultos", "Famílias", "Idosos"],
                    index=0
                )
                
                cta = st.text_input(
                    "**Chamada pra Ação (CTA)**",
                    placeholder="Ex: Agende uma consulta gratuita!",
                    help="Frase de ação que você quer que o leitor execute"
                )
            
            st.markdown("---")
            
            keywords = st.text_area(
                "**Palavras-Chave (SEO)**",
                placeholder="Insira palavras-chave separadas por vírgula\nEx: saúde mental, bem-estar no trabalho, burnout",
                height=80
            )
            
            col3, col4, col5 = st.columns([1,1,2])
            with col3:
                hashtags = st.checkbox("Incluir Hashtags", value=True)
            with col4:
                emojis = st.checkbox("Usar Emojis", value=True)
            
            submitted = st.form_submit_button(
                "GERAR CONTEÚDO →",
                help="Clique para gerar o conteúdo otimizado"
            )
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        return submitted, {
            'topic': topic,
            'platform': platform,
            'tone': tone,
            'length': length,
            'audience': audience,
            'cta': cta,
            'hashtags': hashtags,
            'emojis': emojis,
            'keywords': keywords
        }

def render_result(content, topic):
    st.markdown("""
    <div class="result-container">
        <div class="result-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00d2ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            CONTEÚDO GERADO
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(content, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.download_button(
        label="📥 BAIXAR CONTEÚDO",
        data=content,
        file_name=f"conteudo_seo_{topic[:20]}.md",
        mime="text/markdown"
    )