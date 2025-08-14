import streamlit as st
from llm import generate_content
from frontend import load_css, render_header, render_form, render_result

def main():
    # Configuração inicial
    st.set_page_config(
        page_title="NeuroContent AI",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Carrega o CSS customizado
    load_css()
    
    # Renderiza o cabeçalho
    render_header()
    
    # Renderiza o formulário e obtém os dados
    submitted, form_data = render_form()
    
    # Lógica de submissão
    if submitted:
        if not form_data['topic'].strip():
            st.warning("⚠️ Por favor, insira um tema principal para gerar o conteúdo.")
        else:
            with st.spinner("🧠 NeuroContent AI está criando seu conteúdo perfeito..."):
                try:
                    # Gera o conteúdo usando a função do core
                    content = generate_content(**form_data)
                    
                    # Renderiza o resultado
                    render_result(content, form_data['topic'])
                    
                    # Armazena o tópico na sessão
                    st.session_state.topic = form_data['topic']
                except Exception as e:
                    st.error(f"Ocorreu um erro durante a geração: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()