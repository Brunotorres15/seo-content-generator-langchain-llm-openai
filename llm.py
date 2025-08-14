from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Carregar variáveis de ambiente
load_dotenv()

def generate_content(topic, platform, tone, length, audience, cta, hashtags, emojis, keywords):
    """
    Gera conteúdo SEO usando o modelo Llama 3
    """
    id_model = "gpt-4o-mini" #"llama3-70b-8192"
    llm = ChatOpenAI(
        model=id_model,
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    
    prompt = f"""

    **Instruções Fundamentais:**
    - Responda EXCLUSIVAMENTE no mesmo idioma em que o Tema Principal (topic) está sendo escrito
    - Mantenha consistência linguística com o texto da pergunta
    - Formate a saída em Markdown
    - Mantenha o Texto de forma discursiva e profissional que prenda a atenção à leitura

    Escreva um conteúdo altamente otimizado levando em consideração os seguintes contextos:
    
    Tema Principal: {topic}
    Plataforma: {platform}
    Tom de Voz: {tone}
    Público-Alvo: {audience}
    Extensão: {length}
    {"Use Exatamente esta chamada pra Ação: " + cta if cta else "Sem CTA específico"}
    {"Incluir hashtags relevantes" if hashtags else ""}
    {"Usar emojis para melhor engajamento" if emojis else ""}
    {"Use as Palavras-Chave:" + keywords if keywords else "Nenhuma palavra-chave específica"}
    
    """
    
    res = llm.invoke([
        {"role": "system", "content": "Você é um especialista em Marketing Digital com foco em SEO e escrita persuasiva."},
        {"role": "user", "content": prompt}
    ])
    return res.content