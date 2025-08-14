# SEO Content Generator with LangChain, LLM and OpenAI

![alt text](./imgs/frontend.png)

## 🔍 Project Description
A streamlined content generation tool powered by OpenAI's GPT-4, designed to create SEO-optimized marketing content in multiple languages. The system automatically matches the output language to the input prompt.

## ✨ Core Features
- **Intelligent Content Generation**: Uses OpenAI's GPT-4 to produce high-quality, tailored content
- **Language Matching**: Responds in the same language as the input prompt (Portuguese, English, etc.)
- **SEO Optimization**: Incorporates provided keywords naturally into the content
- **Customizable Output**: Control tone, length, and style for different platforms
- **CTA Integration**: Seamlessly includes calls-to-action when specified

## 🛠️ Technical Implementation
- Built with Python using LangChain's OpenAI integration
- Streamlit-based web interface
- Environment variables for API key management
- Modular architecture separating:
  - Core generation logic (OpenAI)
  - Frontend components
  - Main application flow

## 📂 Code Structure

```
├── core.py # Content generation with OpenAI
├── frontend.py # Streamlit UI components
├── app.py # Main application logic
└── .env # Configuration (OPENAI_API_KEY)
```

## 🤖 How It Works
1. Receives user parameters (topic, keywords, tone, etc.)
2. Constructs optimized prompt for OpenAI
3. Generates content matching the input language
4. Returns formatted Markdown output with:
   - Proper headings
   - Paragraph structure
   - Optional CTAs/hashtags/emojis

## 🌟 Key Differentiators
- Focus on natural language matching (no forced translations)
- Clean Markdown output ready for publishing
- Simple, intuitive interface
- No unnecessary dependencies or complexity

Built with ❤️ using OpenAI's powerful language models