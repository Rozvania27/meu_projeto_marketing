import numpy as np
import pandas as pd

# Define a semente para gerar sempre os mesmos dados
np.random.seed(42)
total_envios = 500

segmentos = ['VIP', 'Novos', 'Inativos', 'Recorrentes']
assuntos = [
    'Oferta Exclusiva de Primavera 🌸',
    'Bem-vindo à nossa loja! 👋',
    'Sentimos sua falta, volte com 10% OFF 🎁',
    'Confira as novidades da semana! 🚀',
]

dados = {
    'id_envio': [f'ENV{str(i).zfill(4)}' for i in range(1, total_envios + 1)],
    'segmento_cliente': np.random.choice(
        segmentos, size=total_envios, p=[0.2, 0.3, 0.25, 0.25]
    ),
    'assunto_email': np.random.choice(assuntos, size=total_envios),
    'abriu': np.random.choice([0, 1], size=total_envios, p=[0.4, 0.6]),
}

df = pd.DataFrame(dados)

# Regra lógica: só clica se abriu, só converte se clicou
df['clicou'] = df['abriu'].apply(
    lambda x: np.random.choice([0, 1], p=[0.6, 0.4]) if x == 1 else 0
)
df['converteu'] = df['clicou'].apply(
    lambda x: np.random.choice([0, 1], p=[0.7, 0.3]) if x == 1 else 0
)

# Salva em um arquivo CSV
df.to_csv('dados_marketing.csv', index=False)
print('✅ Arquivo dados_marketing.csv criado com sucesso!')