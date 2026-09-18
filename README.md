# 📊 Marketing Cloud Data & AI Analytics

<p align="center">
  <strong>Transformando dados de marketing em inteligência executiva com IA Generativa.</strong>
</p>

<p align="center">
  <a href="https://meu-projeto-marketing-ai-analytics.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀_Acessar_Dashboard_Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live App Streamlit">
  </a>
  <a href="https://rozvania27.github.io/meu_projeto_marketing/versao_html/" target="_blank">
    <img src="https://img.shields.io/badge/🌐_Acessar_Versão_Web_HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="Live Web HTML">
  </a>
</p>

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://ai.google.dev/" target="_blank">
    <img src="https://img.shields.io/badge/Google_Gemini-3.6-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Google Gemini">
  </a>
  <a href="https://streamlit.io/" target="_blank">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  </a>
  <a href="https://pandas.pydata.org/" target="_blank">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  </a>
  <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTML" target="_blank">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  </a>
</p>

---

<p align="center">
  <a href="#sobre-o-projeto">Sobre</a> •
  <a href="#solucao-arquitetura">Solução</a> •
  <a href="#funcionalidades-chave">Funcionalidades</a> •
  <a href="#tecnologias-utilizadas">Tecnologias</a> •
  <a href="#execucao-local">Execução</a> •
  <a href="#autora">Autora</a>
</p>

---

## 🔗 Demonstrações Rápidas

| Aplicação | Descrição | Links de Acesso |
| :--- | :--- | :--- |
| 🐍 **Python / Streamlit Cloud** | Dashboard analítico em tempo real integrado ao SDK `google-genai` para geração de relatórios executivos. | [🚀 **Acessar Dashboard Live**](https://meu-projeto-marketing-ai-analytics.streamlit.app/) • [💻 **Ver Código `app.py`**](https://github.com/Rozvania27/meu_projeto_marketing/blob/main/app.py) |
| 🌐 **HTML / Front-End** | Interface web responsiva e interativa voltada para apresentação de KPIs e gráficos via Chart.js. | [🌐 **Acessar App Web**](https://rozvania27.github.io/meu_projeto_marketing/versao_html/) • [💻 **Ver Pasta `versao_html`**](https://github.com/Rozvania27/meu_projeto_marketing/tree/main/versao_html) |

---

## 🎯 Sobre o Projeto

O **Marketing Cloud Data & AI Analytics** é uma solução de inteligência de negócios desenvolvida para resolver a complexidade do acompanhamento de campanhas de marketing em grande escala.

A plataforma automatiza a ingestão, tratamento de métricas e geração de relatórios usando o modelo de linguagem **Google Gemini 3.6**, entregando análises prontas para apoio à decisão de equipes de MarTech e Growth.

### 🌟 Diferenciais Técnicos & Boas Práticas:
* **LLM Ops Integrado:** Integração com o SDK `google-genai`, suporte a fallback de erros e Engenharia de Prompts otimizada.
* **Segurança de Dados:** Proteção de credenciais via `.streamlit/secrets.toml` e sanitização através de `.gitignore` rigoroso.
* **Arquitetura Dual-Stack:** Solução analítica completa em Python + protótipo leve para web em HTML5/JS.

---

## 💡 Problema de Negócio

Equipes de marketing gastam horas consolidadas extraindo planilhas e redigindo pareceres executivos sobre o desempenho de campanhas (CTR, Open Rate, Conversion Rate).

### Como este projeto resolve:
- **Centralização:** Consolida dados brutos de interações e jornadas em visualizações dinâmicas.
- **Automação de Insights:** Substitui análises manuais por relatórios executivos instantâneos gerados por IA.
- **Leitura Intuitiva:** Transforma números em narrativas de negócios claras e focadas em conversão.

---

## 🧩 Solução & Arquitetura

```text
┌──────────────────────────────┐
│     DADOS DE MARKETING       │
│  Campanhas • CTR • Conversões│
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  PROCESSAMENTO (Python/Pandas│
│  Agregação e Limpeza de KPIs │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  IA GENERATIVA (Gemini API)  │
│  Engenharia de Prompts e IA  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  CAMADA DE APRESENTAÇÃO      │
│  Streamlit & Dashboard Web   │
└──────────────────────────────┘
