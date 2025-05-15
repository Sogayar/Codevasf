import pandas as pd

arquivo_erros = "erros.csv"
arquivo_codevasf = "codevasf.csv"

try:
    df_erros = pd.read_csv(arquivo_erros)
    df_codevasf = pd.read_csv(arquivo_codevasf)
except FileNotFoundError as e:
    print(f"Erro: {e}")
    exit()

# Verificando se a coluna "N° instrumento" existe em ambos os arquivos
coluna_instrumento = "Nº Instrumento"
if coluna_instrumento not in df_erros.columns:
    print(f"O arquivo '{arquivo_erros}' precisa conter a coluna '{coluna_instrumento}'.")
    exit()

if coluna_instrumento not in df_codevasf.columns:
    print(f"O arquivo '{arquivo_codevasf}' precisa conter a coluna '{coluna_instrumento}'.")
    exit()

# Buscando os números de instrumento do CSV "erros" no CSV "codevasf"
instrumentos_erros = df_erros[coluna_instrumento].unique()
df_filtrado = df_codevasf[df_codevasf[coluna_instrumento].isin(instrumentos_erros)]

# Verificando se algum número de instrumento foi encontrado
if df_filtrado.empty:
    print("Nenhum número de instrumento do CSV 'erros' foi encontrado no CSV 'codevasf'.")
else:
    print(f"Foram encontrados {len(df_filtrado)} registros correspondentes.")
    
    # Salvando as linhas filtradas em um novo arquivo CSV
    arquivo_saida = "resultados_filtrados.csv"
    df_filtrado.to_csv(arquivo_saida, index=False)
    print(f"As informações correspondentes foram salvas em '{arquivo_saida}'.")
