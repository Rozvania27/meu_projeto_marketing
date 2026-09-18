import os
import pandas as pd
import streamlit as st
from google import genai
from google.genai import types

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title='Marketing Cloud Data & IA',
    page_icon='📈',
    layout='wide'
)

# Estilo visual leve via CSS
st.markdown("""
    <style>
        .metric-card {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 15px;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Principal
st.title('📈 Marketing Cloud Data & IA')
st.caption('Simulador de Portfólio de Ciência de Dados & Marketing Analytics')


# 2. Carregamento dos Dados
@st.cache_data
def carregar_dados():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(diretorio_atual, 'dados_marketing.csv')
    return pd.read_csv(caminho_csv)


try:
    df = carregar_dados()
except FileNotFoundError:
    st.error('❌ Arquivo "dados_marketing.csv" não encontrado!')
    st.stop()

# 3. Barra Lateral (Filtros de Segmento)
st.sidebar.header('🔍 Filtros de Segmento')
st.sidebar.write('Selecione os públicos-alvo para recalcular os KPIs:')

segmentos_disponiveis = df['segmento_cliente'].dropna().unique().tolist()
segmentos_selecionados = []

# Checkboxes na barra lateral
for seg in segmentos_disponiveis:
    if st.sidebar.checkbox(seg, value=True):
        segmentos_selecionados.append(seg)

# Aplica os filtros
df_filtrado = df[df['segmento_cliente'].isin(segmentos_selecionados)]

# Dica de Portfólio na Sidebar
st.sidebar.divider()
st.sidebar.info(
    '💡 **DICA DE PORTFÓLIO**\n\n'
    'Este projeto demonstra como integrar pipelines de **Ciência de Dados (Pandas)** '
    'com relatórios de **IA Generativa (Gemini API)** em uma interface interativa (**Streamlit**).'
)

# 4. Cálculo dos KPIs
total_envios = len(df_filtrado)
aberturas = df_filtrado['abriu'].sum()
cliques = df_filtrado['clicou'].sum()
conversoes = df_filtrado['converteu'].sum()

tx_abertura = (aberturas / total_envios * 100) if total_envios > 0 else 0
tx_clique = (cliques / aberturas * 100) if aberturas > 0 else 0
tx_conversao = (conversoes / cliques * 100) if cliques > 0 else 0

# Exibição dos Cartões (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric('✈️ TOTAL DISPAROS', f'{total_envios:,}')
col2.metric('📬 TAXA ABERTURA', f'{tx_abertura:.1f}%')
col3.metric('🖱️ CTR (CLIQUE/ABERTURA)', f'{tx_clique:.1f}%')
col4.metric('🛒 CONVERSÃO', f'{tx_conversao:.1f}%')

st.divider()

# 5. Gráfico de Desempenho por Segmento
st.subheader('📊 Desempenho por Segmento (%)')
st.caption('Comparativo das taxas de engajamento para os segmentos selecionados')

if not df_filtrado.empty:
    df_grafico = (
        df_filtrado.groupby('segmento_cliente')
        .agg(
            total=('id_envio', 'count'),
            abertos=('abriu', 'sum'),
            clicados=('clicou', 'sum'),
            convertidos=('converteu', 'sum')
        )
        .reset_index()
    )

    df_grafico['Abertura (%)'] = (df_grafico['abertos'] / df_grafico['total']) * 100
    df_grafico['CTR (%)'] = (df_grafico['clicados'] / df_grafico['abertos'].replace(0, 1)) * 100
    df_grafico['Conversão (%)'] = (df_grafico['convertidos'] / df_grafico['clicados'].replace(0, 1)) * 100

    # Exibição do gráfico de colunas
    st.bar_chart(
        df_grafico.set_index('segmento_cliente')[
            ['Abertura (%)', 'CTR (%)', 'Conversão (%)']
        ],
        height=320,
    )
else:
    st.warning('Nenhum segmento selecionado. Marque ao menos uma opção no menu lateral.')

st.divider()

# 6. Relatório Inteligente com IA Generativa
st.subheader('🤖 Relatório de Insights com IA Generativa')
st.caption('Acione a API do Gemini para interpretar as estatísticas filtradas em tempo real')

api_key_input = st.text_input(
    'Digite sua Chave da API do Gemini (GEMINI_API_KEY):', type='password'
)

if st.button('✨ Gerar Análise Executiva'):
    if not api_key_input:
        st.warning('Por favor, digite sua chave da API para continuar.')
    elif df_filtrado.empty:
        st.warning('Selecione pelo menos um segmento na barra lateral.')
    else:
        with st.spinner('Enviando métricas para o Gemini 2.5 Flash & compilando relatório...'):
            try:
                client = genai.Client(api_key=api_key_input)

                prompt = f"""
                Você é um especialista em Marketing Cloud e Ciência de Dados.
                Analise os seguintes dados filtrados de uma campanha e elabore um relatório executivo curto estruturado nos tópicos abaixo:

                1. Pontos Fortes & Destaques
                2. Gargalos Identificados
                3. Recomendações Estratégicas (com ações práticas)

                DADOS FILTRADOS DA CAMPANHA:
                - Segmentos Analisados: {', '.join(segmentos_selecionados)}
                - Total de Envios: {total_envios}
                - Taxa Média de Abertura: {tx_abertura:.2f}%
                - CTR Média: {tx_clique:.2f}%
                - Taxa Média de Conversão: {tx_conversao:.2f}%
                """

                # Configuração para desativar o aviso automático de Function Calling
                config = types.GenerateContentConfig(
                    automatic_function_calling=types.AutomaticFunctionCallingConfig(
                        disable=True
                    )
                )

                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=prompt,
                    config=config
                )

                st.success('Relatório Executivo Gerado pelo Gemini com sucesso!')
                st.markdown(response.text)

            except Exception as e:
                st.error(f'Erro ao conectar com a API do Gemini: {e}')